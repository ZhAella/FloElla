from apscheduler.schedulers.background import BackgroundScheduler
from . import jobs


scheduler = BackgroundScheduler()
scheduler.add_job(jobs.create_days, 'interval', days=1)
scheduler.start()


def stop_scheduler():
    scheduler.shutdown()
