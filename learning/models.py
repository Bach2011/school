from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=1000)
    avg_point = models.FloatField(blank=True, null=True)
    def __str__(self):
        return f"{self.name}"
class Score(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    point = models.FloatField(blank=True, null=True)
    kind = models.IntegerField(default=1)
class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    place = models.CharField(max_length=1000, blank=True)
    kind = models.IntegerField()
