from datetime import date
from .models import MenstrualDayStatus
from users.models import CustomUser


def create_days():
    users_with_last_menstruation = CustomUser.objects.exclude(last_menstruation_date=None)

    for user in users_with_last_menstruation:
        last_menstruation = user.last_menstruation_date.date()
        today = date.today()
        cycle_day = (today - last_menstruation).days

        if cycle_day <= 0:
            continue

        status = 'ordinary_day'
        if cycle_day == 14:
            status = 'ovulation'
        elif cycle_day > 20:
            status = 'period_may_start'
        elif cycle_day > 24:
            status = 'delay_of_menstruation'

        MenstrualDayStatus.objects.create(
            user_id=user,
            status=status,
            date=today
        )
    print('Done')
