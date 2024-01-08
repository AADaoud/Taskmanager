from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'subject', 'dueDate']

    def cleanTaskForm(self):
        data = self.cleaned_data['title', 'description', 'subject', 'dueDate']