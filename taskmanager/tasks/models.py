from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    dueDate = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.title