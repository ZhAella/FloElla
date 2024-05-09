from django.db import models
from users.models import GirlUser


class MenstrualDayStatus(models.Model):
    status_choice = [
        ("Menstrual day", "Menstrual day"),
        ('Follicular phase', 'Follicular phase'),
        ("Delay", "Delay"),
        ("Ovulation", "Ovulation"),
        ("Luteinization", "Luteinization")
    ]
    name = models.CharField(max_length=50, choices=status_choice)
    delay_days = models.IntegerField(blank=True, null=True)
    user_id = models.ForeignKey(GirlUser, on_delete=models.CASCADE)
    date = models.DateField(null=True)

    def __str__(self):
        return f"{self.name} - {self.date}"


class Reminder(models.Model):
    user_id = models.ForeignKey(GirlUser, on_delete=models.CASCADE)
    text = models.TextField()
    data = models.DateField()


class SymptomName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserSymptom(models.Model):
    symptom = models.ForeignKey(SymptomName, on_delete=models.CASCADE)
    user_id = models.ForeignKey(GirlUser, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    is_active = models.BooleanField(default=False)
