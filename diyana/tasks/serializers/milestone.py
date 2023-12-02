from rest_framework_json_api import serializers
from tasks.models import Milestone


class MilestoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milestone
        fields = [
            'name',
            # 'phase',
            'date_detail',
        ]
