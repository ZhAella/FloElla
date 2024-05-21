from rest_framework import generics
from . import serializers


class GirlUserCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.GirlUserCreateSerializer
