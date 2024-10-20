from rest_framework.serializers import ModelSerializer
from .models import Project, ProjectType

class ProjectSerializer(ModelSerializer):
    class meta:
        model = Project
        fields = ['id', 'name', 'description', 'type', 'start_date', 'end_date']