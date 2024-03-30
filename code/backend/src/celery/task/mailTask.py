from celery import Celery
from celery.schedules import crontab
from database.models import UserInfo
from datetime import datetime
import requests

app = Celery('CeleryInstance',broker='redis://localhost:6379/0',backend='redis://localhost:6379/0')

@app.task()
def mailTask():
    current_date = datetime.now().strftime("%Y-%m-%d")
    data = UserInfo.query.filter(UserInfo.last_seen!=current_date).all()
    emails = []
    for i in data:
        emails.append(i.email)
    if not emails:
        return
    requests.post('http://localhost:5000/sendMail',json={"emails":emails})
    