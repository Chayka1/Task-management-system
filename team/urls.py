from django.urls import path

from team.api import TeamAPIView

urlpatterns = [
    path("", TeamAPIView.as_view()),
]
