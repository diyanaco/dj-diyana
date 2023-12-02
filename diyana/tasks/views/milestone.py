from rest_framework_json_api.views import RelationshipView, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from tasks.models import Milestone
from tasks.serializers import MilestoneSerializer


class MilestoneViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
    permission_classes = [IsAuthenticated]


class MilestoneRelationshipView(RelationshipView):
    queryset = Milestone.objects.all()
    self_link_view_name = "milestone-relationships"
