from rest_framework import serializers
from . import models


class MenstrualDayStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MenstrualDayStatus
        fields = ['name', 'date']


class SymptomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Symptom
        fields = ['name', 'is_active']
