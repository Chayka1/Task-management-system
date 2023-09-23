from django.conf import settings
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="admin_of_teams",
    )
    worker = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="worker_of_teams"
    )

    class Meta:
        db_table = "team"


class Task(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    task = models.TextField()

    class Meta:
        db_table = "task"
