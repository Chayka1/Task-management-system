from django.conf import settings
from django.db import models


class Task(models.Model):
    team = models.CharField(max_length=100)
    task = models.TextField()
    worker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name="worker_of_teams",
    )

    class Meta:
        db_table = "task"
