

**Requirements:**
Python Packages:
  django
  celery
  redis
  django-celery-results



**To start the worker:**
celery -A celery_project.celeryconfig worker -n worker1 -l INFO

-n ---> to give a name to the worker in case of multiple workers

**To trigger the beat:**
celery -A celery_project.beat_scheduler beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
