from django.db import models
from users.models import GirlUser


class Status(models.Model):
    name = models.CharField(max_length=50)


class MenstrualDayStatus(models.Model):
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

# class MenstrualDayStatus(models.Model):
#     STATUS_CHOICES = [
#         ("Menstrual day", "Menstrual day"),
#         ("Probably menstruation", "Probably menstruation"),
#         ("Not menstruating", "Not menstruating")
#     ]
#     name = models.CharField(max_length=50, choices=STATUS_CHOICES)
#     user_id = models.ForeignKey(GirlUser, on_delete=models.CASCADE)
#
#
# class Reminder(models.Model):
#     user_id = models.ForeignKey(GirlUser, on_delete=models.CASCADE)
#     text = models.TextField()
#     data = models.DateField()
#
#
# class Symptom(models.Model):
#     name = models.CharField(max_length=100)
#     user_id = models.ForeignKey(GirlUser, on_delete=models.CASCADE)

