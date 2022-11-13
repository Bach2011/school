from django.shortcuts import render, HttpResponseRedirect
from .models import Score, Subject, Exam
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, "learning/index.html")
def scores(request):    
    scores = 0
    times = 0
    for score in Subject.objects.all():
        try:
            scores += score.avg_point
            times += 1
        except:
            continue
        avg = round(scores / times,2)
        a = evaluate(avg)
        return render(request, "learning/scores.html", {
            "subjects": Subject.objects.all(),
            "avg":avg,
            "a":a
        })
def subjects(request):
    if request.method == "POST":
        name = str(request.POST.get('name')).capitalize()
        Subject.objects.create(name=name)
        return HttpResponseRedirect(reverse('subject', args=[Subject.objects.last().id]))
    else:
        return render(request, "learning/subjects.html", {
        "subjects": Subject.objects.all()
    })
def exams(request):
    if request.method == "POST":
        delete = request.POST.get('del')
        if delete is not None:
            exam = Exam.objects.get(id=int(delete))
            exam.delete()
            return HttpResponseRedirect(reverse('exams'))
        else:
            subject = Subject.objects.get(name=str(request.POST.get('subject')))
            date = request.POST.get('date')
            kind = request.POST.get('kind')
            place = request.POST.get('place')
            Exam.objects.create(subject=subject, date=date, kind=kind, place=place)
            return HttpResponseRedirect(reverse('exams'))
    else:
        return render(request, "learning/exams.html", {
            "subjects": Subject.objects.all(),
            "exams": Exam.objects.all()
        })
def subject(request, id):
    sub = Subject.objects.get(pk=id)
    if request.method == "POST":
        score_id = request.POST.get("score")
        if score_id:
            score = Score.objects.get(pk=score_id)
            score.delete()
            sub.avg_point = avg_point(sub)
            sub.save()
        else:
            score = request.POST.get('point')
            kind = request.POST.get('kind')
            Score.objects.create(subject=sub, point=score, kind=kind)
            try:
                sub.avg_point = avg_point(sub)
                sub.save()
            except:
                pass
        return HttpResponseRedirect(reverse('subject', args=[id]))
    else:
        return render(request, "learning/subject.html", {
            "subject":sub,
            "scores": Score.objects.filter(subject=Subject.objects.get(pk=id)),
            "e": evaluate(sub.avg_point)
        })
def avg_point(subject):
    try:
        total_point = 0
        times = 0
        scores = Score.objects.filter(subject=subject)
        for score in scores:
            total_point += int(score.point) * int(score.kind)
            times += score.kind
        return round(total_point / times,2)
    except ZeroDivisionError:
        return "x"

def evaluate(score):
    try:
        if score >= 9:
            a = "Excellent"
        elif score >= 8:
            a = "Good"
        elif score >= 6.5:
            a = "OK"
        else:
            a = "Not Good"
        return a
    except:
        return "Not Defined"