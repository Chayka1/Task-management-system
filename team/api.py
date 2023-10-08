from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from team.models import Team
from team.serializers import TeamSerializer
from users.models import User


class TeamCreateView(CreateAPIView):
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        name = request.data.get("name")
        worker_id = request.data.get("worker")
        task = request.data.get("task")
        admin = request.user

        team = Team.objects.create(name=name, admin=admin, task=task)

        if worker_id:
            try:
                worker = User.objects.get(id=worker_id)
                team.worker = worker
                team.save()
            except User.DoesNotExist:
                return Response(
                    {
                        "detail": f'User with specified ID "{worker_id}" does not exist.'  # noqa
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
