from django.db import models
from users.models import CustomUser


class MenstrualDayStatus(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    STATUS_CHOICES = (
        ('periods', 'Periods.'),
        ('ordinary_day', 'Ordinary Day.'),
        ('ovulation', 'Ovulation.'),
        ('period_may_start', 'Maybe your period will start today.'),
        ('delay_of_menstruation', 'Delay of menstruation.')
    )
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='ordinary_day')
    date = models.DateField(auto_now_add=True)
