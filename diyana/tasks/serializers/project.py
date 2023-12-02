from django.contrib.auth.models import Group
from rest_framework_json_api import relations, serializers
from rest_framework.exceptions import ValidationError
from tasks.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    groups = relations.ResourceRelatedField(
        related_link_view_name="project-related",
        self_link_view_name="project-relationships",
        queryset=Group.objects,
        many=True,
        required=True,
    )

    included_serializers = {
        "groups": "tasks.serializers.GroupSerializer",
    }

    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'groups',
            'url'
        ]

    def create(self, validated_data):
        name: str = validated_data['name']
        # Only accept single word project names
        if ' ' in name:
            raise ValidationError("Project name cannot contain spaces")
        validated_data['code'] = name.upper()
        return super().create(validated_data)
