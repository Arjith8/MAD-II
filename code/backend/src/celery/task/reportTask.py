from celery import Celery
from celery.schedules import crontab
from database.models import UserInfo
from datetime import datetime
import requests

app = Celery('CeleryInstance',broker='redis://localhost:6379/0',backend='redis://localhost:6379/0')

@app.task()
def mailTask():
    data = UserInfo.query.filter(UserInfo.account_type=='creator').all()
    emails = []
    for i in data:
        emails.append(i.email)
    return requests.post('http://localhost:5000/',json={"emails":emails, "purpose":"creator_remainder"})
    pass
    