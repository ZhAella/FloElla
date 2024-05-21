from rest_framework import serializers
from . models import MenstrualDayStatus


class MenstrualDayStatusRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenstrualDayStatus
        fields = ['user_id', 'start_data', 'end_data', 'status']


class MenstrualDayStatusResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenstrualDayStatus
        fields = '__all__'
