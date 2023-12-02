from rest_framework_json_api.views import RelationshipView, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from tasks.models import Phase
from tasks.serializers import PhaseSerializer
class PhaseViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Phase.objects.all()
    serializer_class = PhaseSerializer
    permission_classes = [IsAuthenticated]


class PhaseRelationshipView(RelationshipView):
    queryset = Phase.objects.all()
    self_link_view_name = "phase-relationships"
