from rest_framework_json_api import serializers
from tasks.models import Code


class CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Code
        fields = [
            'name',
            'description',
            'from_type',
            'value_str',
            'value_int',
            'value_bool',
        ]
