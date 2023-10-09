from django.conf import settings
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="admin_of_teams",
    )

    class Meta:
        db_table = "team"
