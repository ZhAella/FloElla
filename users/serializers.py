from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from djoser.serializers import UserCreateSerializer
from . import models


class JwtTokenSerializer(TokenObtainPairSerializer):
    ...


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = models.CustomUser
        fields = ['username', 'password', 'weight',
                  'height', 'age', 'menstruation_start_date',
                  'menstruation_end_date', 'email']


class UserSerializer(serializers.ModelSerializer):
    partial_email = serializers.SerializerMethodField()

    class Meta:
        model = models.CustomUser
        fields = ['id', 'username', 'first_name',
                  'last_name', 'age', 'weight',
                  'height', 'registration_date', 'menstruation_start_date',
                  'menstruation_end_date', 'partial_email']

    @staticmethod
    def get_partial_email(obj):
        if obj.email:
            name, domain = obj.email.split('@')
            if len(name) > 2:
                name = name[:2] + '*' * (len(name) - 2)
            return f"{name}@{domain}"
        return None


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ['id', 'username', 'first_name',
                  'last_name', 'age', 'weight',
                  'height', 'registration_date', 'menstruation_start_date',
                  'menstruation_end_date', 'email']
        extra_kwargs = {
            'password': {'write_only': True},
            'registration_date': {'read_only': True},
            'email': {'write_only': True}
        }
