from rest_framework_json_api import relations, serializers
from tasks.models import DateDetail, Task


class DateDetailSerializer(serializers.ModelSerializer):
    task = relations.ResourceRelatedField(
        related_link_view_name="dates-related",
        # self_link_view_name="dates-relationships",
        queryset=Task.objects,
        required=False,
    )
    included_serializers = {
        'task': 'tasks.serializers.TaskSerializer',
    }

    class Meta:
        model = DateDetail
        fields = [
            'due_date',
            'start_date',
            'reported_date',
            'actual_start_date',
            'actual_end_date',
            'task',
        ]
