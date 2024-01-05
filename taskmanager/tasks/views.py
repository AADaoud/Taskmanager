from django.shortcuts import render
from .models import Task, Subject

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'index.html', {'tasks': tasks, 'subjects': subjects})