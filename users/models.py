from django.db import models
from django.contrib.auth.models import AbstractUser


class GirlUser(AbstractUser):
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    age = models.IntegerField(null=True)
    start_data = models.DateField(auto_now=True, null=True)
    end_data = models.DateField(auto_now=True, null=True)
