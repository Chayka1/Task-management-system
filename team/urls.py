from django.urls import path

from team.api import create_team

urlpatterns = [
    path("", create_team),
]
