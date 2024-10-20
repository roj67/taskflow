from django.db import models

# Create your models here.
class ProjectType(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True)
    type = models.ForeignKey(ProjectType, on_delete=models.CASCADE, related_name='project_type')
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name