from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    height = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)
    last_menstruation_date = models.DateTimeField(null=True, blank=True)

# {
#     "username": "BermetC",
#     "password": "qwerty123",
#     "age": "16",
#     "weight": "50",
#     "height": "168",
#     "last_menstruation_date": "2024-04-20"
#
# }
