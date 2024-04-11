from django.db import models
from django.contrib.auth.models import AbstractUser


class GirlUser(AbstractUser):
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    age = models.IntegerField(max_length=2)
