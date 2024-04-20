from apscheduler.schedulers.background import BackgroundScheduler
from . import jobs

scheduler = BackgroundScheduler()


def start_scheduler():
    # scheduler.add_job(jobs.print_hello, 'interval', minutes=5)
    scheduler.add_job(jobs.update_status, 'interval', minutes=3)
    scheduler.start()


def stop_scheduler():
    scheduler.shutdown()
