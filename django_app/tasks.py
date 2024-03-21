from celery import shared_task
from celery_project import settings

@shared_task(bind=True)
def add_data(self,x, y):
    print(x+y)
    return x+y