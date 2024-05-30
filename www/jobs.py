from datetime import timedelta
from .models import MenstrualDayStatus
from users.models import CustomUser
from django.utils import timezone


def create_days():
    users = CustomUser.objects.all()
    today = timezone.now().date()
    for user in users:
        if user.menstruation_start_date is not None:
            cycle_start = user.menstruation_start_date.date()
            cycle_day = (today - cycle_start).days

            print(cycle_day)

            status = find_status(cycle_day)

            before_date = today - timedelta(days=1)
            before_date_2 = today - timedelta(days=2)
            before_date_3 = today - timedelta(days=3)

            try:
                before_date_status = MenstrualDayStatus.objects.get(user_id=user.id, date=before_date)
            except MenstrualDayStatus.DoesNotExist:
                before_date_status = None

            try:
                before_date_2_status = MenstrualDayStatus.objects.get(user_id=user.id, date=before_date_2)
            except MenstrualDayStatus.DoesNotExist:
                before_date_2_status = None

            try:
                before_date_3_status = MenstrualDayStatus.objects.get(user_id=user.id, date=before_date_3)
            except MenstrualDayStatus.DoesNotExist:
                before_date_3_status = None

            if status == 'periods':
                if ((before_date_status and before_date_status.status == 'periods')
                        or (before_date_2_status and before_date_2_status.status == 'periods')
                        or (before_date_3_status and before_date_3_status.status == 'periods')):
                    pass
                else:
                    user.menstruation_start_date = today
                user.menstruation_end_date = today
            user.save()
            MenstrualDayStatus.objects.create(
                user_id=user,
                status=status,
                date=today)
    print('Done')


def find_status(cycle_day):
    if 1 <= cycle_day <= 5:
        return 'periods'
    elif 6 <= cycle_day <= 12:
        return 'ordinary_day'
    elif 13 <= cycle_day <= 15:
        return 'ovulation'
    elif 15 <= cycle_day <= 28:
        return 'ordinary_day'
    elif cycle_day > 29:
        return 'delay_of_menstruation'
