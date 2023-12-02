from rest_framework_json_api.views import RelationshipView, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from tasks.models import Tag
from tasks.serializers import TagSerializer


class TagViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class TagRelationshipView(RelationshipView):
    queryset = Tag.objects.all()
    self_link_view_name = "grouptask-relationships"
