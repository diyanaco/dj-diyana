from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated
from rest_framework_json_api.views import RelationshipView, ModelViewSet
from rest_framework.authentication import TokenAuthentication
from tasks.serializers import (
    GroupTaskSerializer,
    TaskSerializer,
    SubtaskSerializer,
    UserSerializer,
    GroupSerializer,
    CodeSerializer,
    PrioritySerializer,
    ProjectSerializer,
    PhaseSerializer,
    MilestoneSerializer,
    TagSerializer,
    TemplateSerializer,
    DateDetailSerializer,
)
from tasks.models import (
    Tasklist,
    Task,
    Subtask,
    Code,
    Priority,
    Project,
    User,
    Phase,
    Milestone,
    Tag,
    Template,
    DateDetail,
)


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class TaskViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


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
    permission_classes = [IsAuthenticated]


class SubtaskRelationshipView(RelationshipView):
    queryset = Subtask.objects.all()
    self_link_view_name = "subtask-relationships"


class CodeViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    permission_classes = [IsAuthenticated]


class PriorityViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = [IsAuthenticated]


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


class GroupTaskViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tasklist.objects.all()
    serializer_class = GroupTaskSerializer
    permission_classes = [IsAuthenticated]


class GroupTaskRelationshipView(RelationshipView):
    queryset = Tasklist.objects.all()
    self_link_view_name = "grouptask-relationships"


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


class DateDetailViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DateDetail.objects.all()
    serializer_class = DateDetailSerializer
    permission_classes = [IsAuthenticated]


# class DateDetailRelationshipView(RelationshipView):
#     queryset = DateDetail.objects.all()
#     self_link_view_name = "dates-relationships"
