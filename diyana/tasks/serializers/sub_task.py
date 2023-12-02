from rest_framework_json_api import serializers, relations
from tasks.models import Task, Subtask, Tag, DateDetail 


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
    dates = relations.ResourceRelatedField(
        related_link_view_name="task-related",
        queryset=DateDetail.objects,
        source="date_detail",
    )
    priority_value = serializers.SerializerMethodField()
    included_serializers = {
        "task": "tasks.serializers.TaskSerializer",
        "dates": "tasks.serializers.DateDetailSerializer",
        "tags": "tasks.serializers.TagSerializer",
    }

    class Meta:
        model = Subtask
        fields = [
            'name',
            'description',
            'priority_value',
            'task',
            'reported_by',
            'assigned_to',
            'priority',
            'status',
            'tags',
            'dates',
        ]

    def get_priority_value(self, obj):
        return obj.priority.value_str
