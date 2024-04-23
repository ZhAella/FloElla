from apscheduler.schedulers.background import BackgroundScheduler
from .management.commands import jobs

scheduler = BackgroundScheduler()


def start_scheduler():
    scheduler.add_job(jobs.print_hello, 'interval', seconds=1)
    scheduler.start()


def stop_scheduler():
    scheduler.shutdown()
