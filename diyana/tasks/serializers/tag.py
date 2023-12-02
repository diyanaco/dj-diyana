from rest_framework_json_api import serializers, relations
from tasks.models import Tag, Task, Tasklist, Subtask


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
        queryset=Tasklist.objects,
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
            'name',
            'tasks',
            'groups',
            'subs',
        ]
