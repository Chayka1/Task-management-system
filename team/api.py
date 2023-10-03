from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from team.models import Team
from team.serializers import TeamSerializer


class TeamCreateView(CreateAPIView):
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data["admin"] = request.user.id
        return super().create(request, *args, **kwargs)


class TeamAPIView(ListAPIView):
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]
    queryset = Team.objects.all()

    def post(self, request, *args, **kwargs):
        return TeamCreateView.as_view()(request._request).render()
