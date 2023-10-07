from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from team.models import Team
from team.serializers import TeamSerializer
from users.models import User


class TeamCreateView(CreateAPIView):
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data["admin"] = request.user.id
        return super().create(request, *args, **kwargs)


class TeamAPIView(RetrieveUpdateAPIView):
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]
    queryset = Team.objects.all()

    def post(self, request, *args, **kwargs):
        name = request.data.get("name")
        worker_id = request.data.get("worker")

        try:
            team = Team.objects.get(name=name)
        except Team.DoesNotExist:
            return Response(
                {
                    "detail": f'Team with specified name "{name}" does not exist.'  # noqa
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            worker = User.objects.get(id=worker_id)
        except User.DoesNotExist:
            return Response(
                {
                    "detail": f'User with specified ID "{worker_id}" does not exist.'  # noqa
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        team.worker = worker
        team.save()

        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_200_OK)
