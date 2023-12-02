from rest_framework_json_api import serializers, relations
from tasks.models import Template, Phase


class TemplateSerializer(serializers.ModelSerializer):
    phases = relations.ResourceRelatedField(
        related_link_view_name="template-related",
        self_link_view_name="template-relationships",
        queryset=Phase.objects,
        many=True,
        required=False,
    )

    included_serializers = {
        "phases": "tasks.serializers.PhaseSerializer",
    }

    class Meta:
        model = Template
        fields = ['name', 'description', 'phases']
