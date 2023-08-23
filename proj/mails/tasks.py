import celery
# from celery.decorators import task
from celery import shared_task
# from celery.utils.log import get_task_logger

from .email import send_review_email

# logger = get_task_logger(__name__)


@shared_task
def send_review_email_task(name, email, review):
    return send_review_email(name, email, review)