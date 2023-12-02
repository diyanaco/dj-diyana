from rest_framework_json_api.views import RelationshipView, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from tasks.models import Priority, Milestone
from tasks.serializers import PrioritySerializer


class PriorityViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = [IsAuthenticated]

class PriorityRelationshipView(RelationshipView):
    queryset = Priority.objects.all()
    self_link_view_name = "priority-relationships"
