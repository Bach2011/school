from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('exams', views.exams, name="exams"),
    path('scores', views.scores, name="scores"),
    path("subjects/<int:id>", views.subject, name="subject"),
    path("subjects", views.subjects, name="subjects")
]