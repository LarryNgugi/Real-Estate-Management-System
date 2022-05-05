from apscheduler.schedulers.background import BackgroundScheduler
from . import invoice_update


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(invoice_update.send_reminders, 'interval', seconds=1000)
    scheduler.start()
