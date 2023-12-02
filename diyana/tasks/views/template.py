from rest_framework_json_api.views import RelationshipView, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from tasks.models import Template
from tasks.serializers import TemplateSerializer


class TemplateViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = [IsAuthenticated]


class TemplateRelationshipView(RelationshipView):
    queryset = Template.objects.all()
    self_link_view_name = "template-relationships"
