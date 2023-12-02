from rest_framework_json_api.views import RelationshipView, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from tasks.models import Tasklist
from tasks.serializers import TasklistSerializer
class TasklistViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tasklist.objects.all()
    serializer_class = TasklistSerializer
    permission_classes = [IsAuthenticated]


class TasklistRelationshipView(RelationshipView):
    queryset = Tasklist.objects.all()
    self_link_view_name = "tasklist-relationships"
