from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers import SchedulerNotRunningError
from . import jobs


scheduler = BackgroundScheduler()

# scheduler.add_job(jobs.create_days, 'interval', minutes=0.1)
scheduler.add_job(jobs.create_days, 'interval', days=1)


def start_scheduler():
    if not scheduler.running:
        scheduler.start()


def stop_scheduler():
    try:
        scheduler.shutdown()
    except SchedulerNotRunningError:
        pass
