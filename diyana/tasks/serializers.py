from django.contrib.auth.models import User, Group
from rest_framework import serializers

from tasks.models import (
    Task,
    Code,
    Priority,
    Project,
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

    class Meta:
        model = Task
        fields = [
            'url',
            'name',
            'description',
            'status',
            'priority',
            'group',
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


class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = [
            'url',
            'name',
            'description',
            'code',
        ]