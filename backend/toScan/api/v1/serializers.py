from rest_framework import serializers
from toScan.models import ListToValidate


class ListToValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListToValidate
        fields = "__all__"
