from rest_framework_json_api import serializers
from tasks.models import Priority


class PrioritySerializer(serializers.ModelSerializer):

    class Meta:
        model = Priority
        fields = [
            'urgency',
            'gravity',
            'criticality',
            'value_str',
            'value_int',
        ]
