from django.urls import path

from task.api import TaskCreateView

urlpatterns = [
    path("", TaskCreateView.as_view()),
]
