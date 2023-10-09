from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from team.models import Team
from team.serializers import TeamSerializer


class TeamCreateView(CreateAPIView):
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        name = request.data.get("name")
        admin = request.user

        if Team.objects.filter(name=name):
            return Response({"detail": f"This team {name} was been created!"})
        else:
            team = Team.objects.create(name=name, admin=admin)

        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
