from rest_framework import serializers
from . import models


class MenstrualDayStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MenstrualDayStatus
        fields = ['name', 'date']

    name = serializers.CharField(required=False)
    date = serializers.DateField(required=False)


class SymptomNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SymptomName
        fields = "__all__"


class SymptomResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    symptom = SymptomNameSerializer()
    is_active = serializers.BooleanField()
