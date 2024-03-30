from celery import Celery
from celery.schedules import crontab

app = Celery('CeleryInstance',broker='redis://localhost:6379/0',backend='redis://localhost:6379/0')


app.conf.beat_schedule = {
    'User-Login-Reminder': {
        'task':'tasks.mailTask',
        'schedule':crontab(hour=23,minute=59),
    }
}