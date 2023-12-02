from rest_framework.permissions import IsAuthenticated
from rest_framework_json_api.views import RelationshipView, ModelViewSet
from tasks.models import Subtask
from tasks.serializers import SubtaskSerializer


class SubtaskViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer
    permission_classes = [IsAuthenticated]


class SubtaskRelationshipView(RelationshipView):
    queryset = Subtask.objects.all()
    self_link_view_name = "subtask-relationships"
