from rest_framework import serializers


class BillSerializer(serializers.Serializer):
    client_org = serializers.CharField(max_length=50)
    bill_number = serializers.IntegerField()
    bill_sum = serializers.IntegerField()
    bill_date = serializers.DateField()
