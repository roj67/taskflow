from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.ProjectView.as_view(), name='project-list')
]