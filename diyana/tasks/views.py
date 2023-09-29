from django.contrib.auth.models import Group
from rest_framework import permissions
from rest_framework_json_api.views import RelationshipView, ModelViewSet

from tasks.serializers import (
    UserSerializer,
    GroupSerializer,
    TaskSerializer,
    CodeSerializer,
    PrioritySerializer,
    ProjectSerializer,
    SubtaskSerializer,
    PhaseSerializer
)
from tasks.models import (
    Task,
    Code,
    Priority,
    Project,
    User,
    Subtask,
    Phase,
)


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskRelationshipView(RelationshipView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Task.objects.all()
    self_link_view_name = "task-relationships"


class SubtaskViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class SubtaskRelationshipView(RelationshipView):
    queryset = Subtask.objects.all()
    self_link_view_name = "subtask-relationships"

class CodeViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    permission_classes = [permissions.IsAuthenticated]


class PriorityViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = [permissions.IsAuthenticated]

class PhaseViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Phase.objects.all()
    serializer_class = PhaseSerializer
    permission_classes = [permissions.IsAuthenticated]

class PhaseRelationshipView(RelationshipView):
    queryset = Phase.objects.all()
    self_link_view_name = "phase-relationships"

class ProjectViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProjectRelationshipView(RelationshipView):
    queryset = Project.objects.all()
    self_link_view_name = "project-relationships"