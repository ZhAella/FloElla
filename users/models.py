from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    height = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)
    menstruation_start_date = models.DateTimeField(null=True, blank=True)
    menstruation_end_date = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.username
