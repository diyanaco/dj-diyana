from rest_framework_json_api import serializers, relations
from tasks.models import Phase, Project, Tasklist, DateDetail


class PhaseSerializer(serializers.ModelSerializer):

    projects = relations.ResourceRelatedField(
        related_link_view_name="phase-related",
        self_link_view_name="phase-relationships",
        queryset=Project.objects,
        many=True,
        required=False,
    )

    groups = relations.ResourceRelatedField(
        related_link_view_name="phase-related",
        self_link_view_name="phase-relationships",
        queryset=Tasklist.objects,
        many=True,
        required=False,
    )
    dates = relations.ResourceRelatedField(
        related_link_view_name="task-related",
        queryset=DateDetail.objects,
        source="date_detail",
    )

    priority_value = serializers.SerializerMethodField()

    class Meta:
        model = Phase
        fields = [
            'name',
            'description',
            'priority_value',
            'priority',
            'projects',
            'groups',
            'dates',
        ]

    def get_priority_value(self, obj):
        return obj.priority.value_str
