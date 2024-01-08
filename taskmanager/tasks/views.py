from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Subject
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'index.html', {'tasks': tasks, 'subjects': subjects})

def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks/')
    else:
        form = TaskForm()  
    return render(request, 'create_task.html')

def updateTask(request, id):
    task = get_object_or_404(Task, pk = id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('tasks/')
    else:
        form = TaskForm(instance=Task)
    return render(request, 'templates/update_task.html', {'form': form})

def deleteTask(request, id):
    task = get_object_or_404(Task, pk = id)
    if request.method == 'POST':
        task.delete()
    return redirect('tasks/')
