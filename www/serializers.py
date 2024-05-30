from rest_framework import serializers
from www.models import MenstrualDayStatus, Symptom


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = '__all__'


class MenstrualDayStatusSerializer(serializers.ModelSerializer):
    symptoms = SymptomSerializer(many=False, read_only=True)

    class Meta:
        model = MenstrualDayStatus
        fields = ['id', 'user_id', 'status', 'date', 'symptoms']
