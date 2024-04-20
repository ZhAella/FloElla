from apscheduler.schedulers.background import BackgroundScheduler
from . import jobs

scheduler = BackgroundScheduler()


def start_scheduler():
    scheduler.add_job(jobs.print_hello, 'interval', seconds=1)
    scheduler.start()


def stop_scheduler():
    scheduler.shutdown()
