from django.contrib.auth.models import Group
from rest_framework_json_api import serializers, relations

from tasks.models import (
    Task,
    Subtask,
    Code,
    Priority,
    Project,
    User,
    Phase
)


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ['url', 'name']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    subs = relations.ResourceRelatedField(
        related_link_view_name="task-related",
        self_link_view_name="task-relationships",
        queryset=Subtask.objects,
        many=True,
        required=False,
    )
    included_serializers = {
        "subs": "tasks.serializers.SubtaskSerializer",
    }
    class Meta:
        model = Task
        fields = [
            'id',
            'url',
            'name',
            'description',
            'status',
            'priority',
            'group',
            'subs',
        ]

class SubtaskSerializer(serializers.HyperlinkedModelSerializer):
    task = relations.ResourceRelatedField(
        related_link_view_name="subtask-related",
        self_link_view_name="subtask-relationships",
        queryset=Task.objects,
    )
    included_serializers = {
        "task": "tasks.serializers.TaskSerializer",
    }

    class Meta :
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
            'date_details',
            'tag',
        ]

class CodeSerializer(serializers.HyperlinkedModelSerializer):

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


class PrioritySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Priority
        fields = [
            'urgency',
            'gravity',
            'criticality',
            'value_str',
            'value_int',
        ]

class PhaseSerializer(serializers.HyperlinkedModelSerializer):

    project = relations.ResourceRelatedField(
        related_link_view_name="phase-related",
        self_link_view_name="phase-relationships",
        queryset=Project.objects,
    )
    class Meta:
        model = Phase
        fields = [
            'url',
            'name',
            'description',
            'priority',
            'project',
            'date_details',
        ]

class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = [
            'url',
            'name',
            'description',
            'code',
        ]