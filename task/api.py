from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from task.models import Task
from task.serializers import TaskSerializer
from users.models import User


class TaskCreateView(CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        team = request.data.get("team")
        worker_id = request.data.get("worker")
        task_for_worker = request.data.get("task")

        if Task.objects.filter(team=team):
            return Response(
                {"detail": f"This team {team} does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
        else:
            team_tasks = Task.objects.create(team=team, task=task_for_worker)

        if worker_id:
            try:
                worker = User.objects.get(id=worker_id)
                team_tasks.worker = worker
                team_tasks.save()
            except User.DoesNotExist:
                return Response(
                    {
                        "detail": f'User with specified ID "{worker_id}" does not exist.'  # noqa
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

        serializer = TaskSerializer(team_tasks)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
