from django.db import models
from django.contrib.auth.models import AbstractUser


class GirlUser(AbstractUser):
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.IntegerField(max_length=3)
    start_data = models.DateField(auto_now=True)
    end_data = models.DateField(auto_now=True)
