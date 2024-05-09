from django.utils import timezone
from datetime import timedelta
from users.models import GirlUser
from . import models


def update_status():
    today = timezone.now().date()
    users = GirlUser.objects.all()

    for user in users:
        last_menstrual_day = user.end_date
        if last_menstrual_day is not None:
            duration = (last_menstrual_day - user.start_date).days + 1
            follicular_phase_days = 14 - duration
            follicular_phase = user.start_date + timedelta(days=duration)

            next_menstrual_day = last_menstrual_day + timedelta(days=28)
            ovulation = last_menstrual_day + timedelta(days=follicular_phase_days)
            luteinization = ovulation + timedelta(days=3)

            current_status = None
            delay_days = None

            if today >= next_menstrual_day:
                delay = (today - next_menstrual_day).days
                delay_days = delay + 1
                current_status = "Delay"
            elif ovulation > today >= follicular_phase:
                current_status = 'Follicular phase'
            elif luteinization > today >= ovulation:
                current_status = 'Ovulation'
            elif today >= luteinization:
                current_status = 'Luteinization'
            print(current_status)
            if current_status is not None:
                models.MenstrualDayStatus.objects.create(
                    name=current_status,
                    delay_days=delay_days,
                    user_id=user,
                    date=today
                )
                print('Changed')

