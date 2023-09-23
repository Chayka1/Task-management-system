from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Team


@permission_classes([IsAuthenticated])
def create_team(request):
    if request.method == "POST":
        name = request.POST.get("name")
        admin = request.user

        team = Team.objects.create(name=name, admin=admin)
        team.workers.add(request.user)
