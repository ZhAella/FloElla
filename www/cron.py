from django_cron import CronJobBase, Schedule
from django.utils import timezone
from datetime import timedelta
from users.models import GirlUser
from . import models


class UpdateStatusCronJob(CronJobBase):
    RUN_EVERY_MINS = 60 * 24
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'www.update_status_cron_job'

    @staticmethod
    def do():
        today = timezone.now().date()
        users = GirlUser.objects.all()

        for user in users:
            last_menstrual_day = models.MenstrualDayStatus.objects.filter(
                user_id=user.id,
                name='Menstrual day'
            ).order_by('-created_date').first()

            if last_menstrual_day:
                next_menstrual_day = last_menstrual_day.created_date + timedelta(days=28) + timedelta(days=28)

                if today >= next_menstrual_day.date():
                    models.MenstrualDayStatus.objects.create(
                        name='Probably menstruation',
                        user_id=user
                    )
