from django.core.management.base import BaseCommand
from datetime import timedelta
from www.models import MenstrualDayStatus
from users.models import GirlUser


class Command(BaseCommand):
    help = 'Generate MenstrualDayStatus objects for each day of the menstrual cycle'

    def handle(self, *args, **options):
        users = GirlUser.objects.all()
        for user in users:
            start_date = user.start_data

            for i in range(28):
                day = start_date + timedelta(days=i)
                status = "Menstrual day" if i < 5 else "Not menstruating"
                MenstrualDayStatus.objects.create(name=status, user_id=user)

