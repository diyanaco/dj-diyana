from rest_framework_json_api.views import RelationshipView, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from tasks.models import Project
from tasks.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer
    authentication_classes =  [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = ProjectSerializer(self.queryset, many=True, context={'request': request})
        if serializer.is_valid():
            return self.list(request, *args, **kwargs)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectRelationshipView(RelationshipView):
    queryset = Project.objects.all()
    self_link_view_name = "project-relationships"
