from django.db import models
from authentication.models import User
from project.models import Project

# Create your models here.
class TaskType(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
    assigned_users = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='assigned_user')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
