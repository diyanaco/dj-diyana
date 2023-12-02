from rest_framework_json_api import serializers, relations
from tasks.models import Tasklist, Tag, Task, Phase


class TasklistSerializer(serializers.ModelSerializer):
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
        related_link_view_name="grouptask-related",
        self_link_view_name="grouptask-relationships",
        queryset=Phase.objects,
        required=False,
    )
    included_serializers = {
        "tags": "tasks.serializers.TagSerializer",
        "tasks": "tasks.serializers.TaskSerializer",
    }

    class Meta:
        model = Tasklist
        fields = [
            'name',
            'description',
            'phase',
            'tasks',
            'tags',
            'date_detail',
        ]
