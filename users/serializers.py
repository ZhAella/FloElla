from djoser.serializers import UserCreateSerializer
from . import models


class GirlUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = models.GirlUser
        fields = ['email', 'username', 'password',
                  'weight', 'height', 'age',
                  'start_date', 'end_date']
