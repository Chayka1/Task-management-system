from django.urls import path

from team.api import TeamCreateView

urlpatterns = [
    path("", TeamCreateView.as_view()),
]
