from __future__ import absolute_import, unicode_literals
import os
import json
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')

app = Celery('celery_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

def setup_periodic_tasks():
    from django_celery_beat.models import CrontabSchedule, PeriodicTask
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute='1',
        hour='*',
        day_of_week='*',
        day_of_month='*',
        month_of_year='*',
    )
    PeriodicTask.objects.create(
        crontab=schedule,
        name='Adding numbers',
        task='django_app.tasks.add_data',
        args=json.dumps([3, 5]),  
    )

@app.on_after_configure.connect
def periodic_tasks(sender, **kwargs):
    setup_periodic_tasks()
