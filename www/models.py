from django.db import models
from users.models import GirlUser


class MenstrualDayStatus(models.Model):
    status_choice = {
        "Menstrual day": "Menstrual day",
        "Probably menstruation": "Probably menstruation",
        "Not menstruating": "Not menstruating"
    }
    name = models.CharField(max_length=50, choices=status_choice)
    user_id = models.ForeignKey(GirlUser, on_delete=models.CASCADE)


class Reminder(models.Model):
    user_id = models.ForeignKey(GirlUser, on_delete=models.CASCADE)
    text = models.TextField()
    data = models.DateField()


class Symptom(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(GirlUser, on_delete=models.CASCADE)
