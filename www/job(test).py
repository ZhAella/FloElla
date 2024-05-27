import os
import django
import logging
from datetime import timedelta
from django.utils import timezone
from . import models

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FloElla.settings')
django.setup()

logger = logging.getLogger('www.job(test)')


def test_job():
    print('I am working...')
    # menstrual_cycles = models.MenstrualDayStatus.objects.all()
    #
    # for cycle in menstrual_cycles:
    #     last_cycle_end = cycle.end_data
    #     today = timezone.now().date()
        #
        # days_since_last_cycle = (today - last_cycle_end).days
        #
        # logger.debug(f"Days since last cycle for user {cycle.user_id}: {days_since_last_cycle}")
        #
        # if True:
        #     new_cycle = models.MenstrualDayStatus.objects.create(
        #         user_id=cycle.user_id,
        #         start_data=today,
        #         end_data=today + timedelta(days=28),
        #         status=models.Status.objects.get(name='New')
        #     )
        #     new_cycle.save()
        #
        #     models.Reminder.objects.create(
        #         user_id=cycle.user_id,
        #         text='Your menstrual cycle has started.',
        #         data=today
        #     )
        #
        #     cycle.status = models.Status.objects.get(name='Completed')
        #     cycle.save()
        #
        #     logger.info(f"New menstrual cycle started for user {cycle.user_id}")
