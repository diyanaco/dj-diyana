from rest_framework_json_api.views import RelationshipView, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from tasks.models import DateDetail
from tasks.serializers import DateDetailSerializer


class DateDetailViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DateDetail.objects.all()
    serializer_class = DateDetailSerializer
    permission_classes = [IsAuthenticated]
