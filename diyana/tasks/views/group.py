from rest_framework_json_api.views import RelationshipView, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group
from tasks.serializers import GroupSerializer


class GroupViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # authentication_classes =  [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class GroupRelationshipView(RelationshipView):
    queryset = Group.objects.all()
    self_link_view_name = "group-relationships"
