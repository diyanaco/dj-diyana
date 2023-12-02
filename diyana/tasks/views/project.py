from rest_framework_json_api.views import RelationshipView, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from tasks.models import Project
from tasks.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # authentication_classes =  [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ProjectRelationshipView(RelationshipView):
    queryset = Project.objects.all()
    self_link_view_name = "project-relationships"
