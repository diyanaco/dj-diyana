from rest_framework_json_api import relations, serializers
from tasks.models import Project
from django.contrib.auth.models import Group


class GroupSerializer(serializers.ModelSerializer):
    projects = relations.ResourceRelatedField(
        related_link_view_name="group-related",
        self_link_view_name="group-relationships",
        queryset=Project.objects,
        many=True,
        required=False,
    )
    included_serializers = {
        "projects": "tasks.serializers.ProjectSerializer",
    }

    class Meta:
        model = Group
        fields = ['name', 'projects']
