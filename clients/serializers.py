from rest_framework import serializers


class ClientSerializer(serializers.Serializer):
    client_name = serializers.CharField(max_length=30)
    organization_count = serializers.IntegerField()
    bills_sum = serializers.IntegerField()
