from django.shortcuts import render
from .models import Task


def index(reguest):
    tasks = Task.objects.all()
    return render(reguest,'main/index.html', {'title': 'головна сторінка сайта', 'tasks': tasks})


def about(reguest):
    return render(reguest,'main/about.html')