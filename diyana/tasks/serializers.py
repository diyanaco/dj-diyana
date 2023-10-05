from django.contrib.auth.models import Group
from rest_framework_json_api import serializers, relations

from tasks.models import (
    GroupTask,
    Task,
    Subtask,
    Code,
    Priority,
    Project,
    User,
    Phase,
    DateDetail,
    Milestone,
    Tag,
)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['url', 'name']


class TaskSerializer(serializers.ModelSerializer):
    subs = relations.ResourceRelatedField(
        related_link_view_name="task-related",
        self_link_view_name="task-relationships",
        queryset=Subtask.objects,
        many=True,
        required=False,
    )

    tags = relations.ResourceRelatedField(
        related_link_view_name="task-related",
        self_link_view_name="task-relationships",
        queryset=Tag.objects,
        many=True,
        required=False,
    )
    # date_detail = relations.ResourceRelatedField(
    #     related_link_view_name="task-related",
    #     self_link_view_name="task-relationships",
    #     queryset=DateDetail.objects,
    #     source="date_detail",
    # )

    included_serializers = {
        "subs": "tasks.serializers.SubtaskSerializer",
        "tags": "tasks.serializers.TagSerializer",
        # "datedetail": "tasks.serializers.DateDetailSerializer"
    }

    class Meta:
        model = Task
        fields = [
            'url',
            'assigned_to',
            'reported_by',
            'url',
            'name',
            'description',
            'status',
            'priority',
            'group',
            'subs',
            'tags',
            'date_detail',
        ]


class SubtaskSerializer(serializers.ModelSerializer):
    task = relations.ResourceRelatedField(
        related_link_view_name="subtask-related",
        self_link_view_name="subtask-relationships",
        queryset=Task.objects,
    )
    tags = relations.ResourceRelatedField(
        related_link_view_name="subtask-related",
        self_link_view_name="subtask-relationships",
        queryset=Tag.objects,
        many=True,
        required=False,
    )
    included_serializers = {
        "task": "tasks.serializers.TaskSerializer",
        # "date_detail": "tasks.serializers.DateDetailSerializer",
        "tags": "tasks.serializers.TagSerializer",
    }

    class Meta:
        model = Subtask
        fields = [
            'url',
            'name',
            'description',
            'task',
            'reported_by',
            'assigned_to',
            'priority',
            'status',
            'tags',
            'date_detail',
        ]


class CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Code
        fields = [
            'url',
            'name',
            'description',
            'from_type',
            'value_str',
            'value_int',
            'value_bool',
        ]


class PrioritySerializer(serializers.ModelSerializer):

    class Meta:
        model = Priority
        fields = [
            'url'
            'urgency',
            'gravity',
            'criticality',
            'value_str',
            'value_int',
        ]


class PhaseSerializer(serializers.ModelSerializer):

    projects = relations.ResourceRelatedField(
        related_link_view_name="phase-related",
        self_link_view_name="phase-relationships",
        queryset=Project.objects,
        many=True,
        required=False,
    )

    groups = relations.ResourceRelatedField(
        related_link_view_name = "phase-related",
        self_link_view_name = "phase-relationships",
        queryset = GroupTask.objects,
        many = True,
        required = False,
    )


    class Meta:
        model = Phase
        fields = [
            'url',
            'name',
            'description',
            'priority',
            'projects',
            'groups',
            'date_detail',
        ]


class ProjectSerializer(serializers.ModelSerializer):
    teams = relations.ResourceRelatedField(
        related_link_view_name="project-related",
        self_link_view_name="project-relationships",
        queryset=Group.objects,
        many=True,
        required=False,
    )
    phases = relations.ResourceRelatedField(
        related_link_view_name="project-related",
        self_link_view_name="project-relationships",
        queryset=Phase.objects,
        many=True,
        required=False,
    )
    # templates = relations.Re

    included_serializers = {
        "teams": "tasks.serializers.GroupSerializer",
        "phases": "tasks.serializers.PhaseSerializer",
    }

    class Meta:
        model = Project
        fields = [
            'url',
            'name',
            'description',
            'teams',
            'phases',
            'code',
        ]


class DateDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = DateDetail
        fields = [
            'url',
            'from_type',
            'due_date',
            'start_date',
            'reported_date',
            'actual_start_date',
            'actual_end_date',
        ]


class PrioritySerializer(serializers.ModelSerializer):

    class Meta:
        model = Priority
        fields = [
            'url',
            'urgency',
            'gravity',
            'criticality',
            'value_int',
            'value_str',
        ]


class MilestoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milestone
        fields = [
            'url',
            'name',
            'phase',
            'date_detail',
        ]


class GroupTaskSerializer(serializers.ModelSerializer):
    tags = relations.ResourceRelatedField(
        related_link_view_name="grouptask-related",
        self_link_view_name="grouptask-relationships",
        queryset=Tag.objects,
        many=True,
        required=False,
    )
    tasks = relations.ResourceRelatedField(
        related_link_view_name="grouptask-related",
        self_link_view_name="grouptask-relationships",
        queryset=Task.objects,
        many=True,
        required=False,
    )
    phase = relations.ResourceRelatedField(
        related_link_view_name = "grouptask-related",
        self_link_view_name = "grouptask-relationships",
        queryset = Phase.objects,
        required = False,
    )
    included_serializers = {
        "tags": "tasks.serializers.TagSerializer",
        "tasks": "tasks.serializers.TaskSerializer",
    }
        

    class Meta:
        model = GroupTask
        fields = [
            'url',
            'name',
            'description',
            'phase',
            'tasks',
            'tags',
            'date_detail',
        ]


class TagSerializer(serializers.ModelSerializer):
    tasks = relations.ResourceRelatedField(
        related_link_view_name="tag-related",
        self_link_view_name="tag-relationships",
        queryset=Task.objects,
        many=True,
        required=False,
        source="tag_tasks",
    )
    groups = relations.ResourceRelatedField(
        related_link_view_name="tag-related",
        self_link_view_name="tag-relationships",
        queryset=GroupTask.objects,
        many=True,
        required=False,
        source="tag_grouptasks",
    )
    subs = relations.ResourceRelatedField(
        related_link_view_name="tag-related",
        self_link_view_name="tag-relationships",
        queryset=Subtask.objects,
        many=True,
        required=False,
        source="tag_subtasks",
    )

    included_serializers = {
        "tasks": "tasks.serializers.TaskSerializer",
        "groups": "tasks.serializers.GroupTaskSerializer",
        "subs": "tasks.serializers.SubtaskSerializer",
    }

    class Meta:
        model = Tag
        fields = [
            'url',
            'name',
            'tasks',
            'groups',
            'subs',
        ]
