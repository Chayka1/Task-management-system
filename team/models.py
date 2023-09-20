from django.db import models

from users.models import User


class Team(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="admin_of_teams"
    )
    worker = models.ManyToManyField(User, related_name="worker_of_teams")

    class Meta:
        db_table = "teams"


class Task(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.TextField()

    class Meta:
        db_table = "tasks"
