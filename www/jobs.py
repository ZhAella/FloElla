from django.utils import timezone
from datetime import timedelta
from users.models import GirlUser
from . import models


def update_status():
    today = timezone.now().date()
    users = GirlUser.objects.all()

    for user in users:
        last_menstrual_day = GirlUser.end_data

        if last_menstrual_day:
            next_menstrual_day = last_menstrual_day + timedelta(days=28)

            if today >= next_menstrual_day.date():
                models.MenstrualDayStatus.objects.create(
                    name='Probably menstruation',
                    user_id=user
                )
            print('Changed')

# def print_hello():
#     print("HELLO")
