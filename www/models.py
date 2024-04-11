from django.db import models
from users.models import GirlUser


class Status(models.Model):
    name = models.CharField(max_length=50)


class MenstrualCycle(models.Model):
    user_id = models.ForeignKey(GirlUser, on_delete=models.CASCADE)
    start_data = models.DateField(auto_now=True)
    end_data = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


class Reminder(models.Model):
    user_id = models.ForeignKey(GirlUser, on_delete=models.CASCADE)
    text = models.TextField()
    data = models.DateField()


class Symptom(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(GirlUser, on_delete=models.CASCADE)
