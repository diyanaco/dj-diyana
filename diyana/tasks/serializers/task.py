from rest_framework_json_api import relations, serializers
from tasks.models import Task, Subtask, Tag, DateDetail, Priority
from datetime import datetime

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
    dates = relations.ResourceRelatedField(
        related_link_view_name="task-related",
        queryset=DateDetail.objects,
        source="date_detail",
    )
    priority_value = serializers.SerializerMethodField()

    included_serializers = {
        "subs": "tasks.serializers.SubtaskSerializer",
        "tags": "tasks.serializers.TagSerializer",
        "dates": "tasks.serializers.DateDetailSerializer"
    }

    class Meta:
        model = Task
        fields = [
            'assigned_to',
            'reported_by',
            'name',
            'description',
            'priority_value',
            'status',
            'priority',
            'subs',
            'tags',
            'dates',
        ]
        # lookup_field = 'pk'

    def create(self, validated_data):
        initial_priority = Priority(urgency=0,
                                    gravity=0,
                                    criticality=0,
                                    value_str="Low")
        initial_priority.save()
        validated_data['priority'] = initial_priority

        date_detail = DateDetail(reported_date=datetime.today())
        date_detail.save()
        validated_data['date_detail'] = date_detail
        return super().create(validated_data)

    def get_priority_value(self, obj):
        return obj.priority.value_str
