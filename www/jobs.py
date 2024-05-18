from datetime import timedelta
from django.utils import timezone
from models import MenstrualDayStatus, Status, Reminder
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FloElla.settings')
django.setup()


def count_days():
    menstrual_cycles = MenstrualDayStatus.objects.all()

    for cycle in menstrual_cycles:
        last_cycle_end = cycle.end_data
        today = timezone.now().date()

        days_since_last_cycle = (today - last_cycle_end).days

        if days_since_last_cycle >= 28:

            new_cycle = MenstrualDayStatus.objects.create(
                user_id=cycle.user_id,
                start_data=today,
                end_data=today + timedelta(days=28),
                status=Status.objects.get(name='New')
            )

            Reminder.objects.create(
                user_id=cycle.user_id,
                text='Your menstrual cycle has started.',
                data=today
            )

            cycle.status = Status.objects.get(name='Completed')
            cycle.save()



