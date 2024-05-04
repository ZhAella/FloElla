from django.db import models
from users.models import GirlUser


class MenstrualDayStatus(models.Model):
    status_choice = [
        ("Menstrual day", "Menstrual day"),
        ("Delay", "Delay"),
        ("Ovulation", "Ovulation"),
        ("Luteinization", "Luteinization")
    ]
    name = models.CharField(max_length=50, choices=status_choice)
    delay_days = models.IntegerField(blank=True, null=True)
    user_id = models.ForeignKey(GirlUser, on_delete=models.CASCADE)
    date = models.DateField(null=True)


class Reminder(models.Model):
    user_id = models.ForeignKey(GirlUser, on_delete=models.CASCADE)
    text = models.TextField()
    data = models.DateField()


class Symptom(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(GirlUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
