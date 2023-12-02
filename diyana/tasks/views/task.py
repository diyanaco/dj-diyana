from rest_framework_json_api.views import RelationshipView, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from tasks.models import Task
from tasks.serializers import TaskSerializer

class TaskViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class TaskRelationshipView(RelationshipView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Task.objects.all()
    self_link_view_name = "task-relationships"
