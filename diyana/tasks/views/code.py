from rest_framework_json_api.views import RelationshipView, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from tasks.models import Code
from tasks.serializers import CodeSerializer


class CodeViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    permission_classes = [IsAuthenticated]
