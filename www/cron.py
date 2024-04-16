from django_cron import CronJobBase, Schedule
from django.utils import timezone
from datetime import timedelta
from . import models


def change_status():
    today = timezone.now().date()
    users = models.MenstrualCycle.objects.values('user_id')

    for user in users:
        cycle = models.MenstrualCycle.objects.filter(user_id=user['user_id']).order_by('-end_data').first()
        if cycle:
            if (today - cycle.end_data).days == 0:
                models.Status.objects.create(name='Фолликулярная фаза')

            elif (today - cycle.end_data).days == 3:
                models.Status.objects.create(name='Овуляция')

            elif (today - cycle.end_data).days == 17:
                models.Status.objects.create(name='Лютеиновая фаза')


# class UpdateStatusCronJob(CronJobBase):
#     RUN_EVERY_MINS = 60 * 24
#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'www.update_status_cron_job'
#
#     def do(self):
#         change_status()


class UpdateStatusCronJob(CronJobBase):
    RUN_EVERY_MINS = 60 * 24
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'www.update_status_cron_job'

    @staticmethod
    def do():
        cycles_to_update = models.MenstrualCycle.objects.filter(
            status__name='Menstruation Ended',
            end_data__lte=(timezone.now() - timedelta(days=28))
        )

        new_status = models.Status.objects.get(name='Menstruation Started')
        for cycle in cycles_to_update:
            cycle.status = new_status
            cycle.save()
