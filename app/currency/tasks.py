from time import sleep

from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task


@shared_task
def debug():
    sleep(10)
    print('DEBUG\n' * 10)


@shared_task(autoretry_for=(ConnectionError,), retry_kwargs={
    'max_retries': 5
})
def send_email_in_background(subject, body):
    raise ConnectionError

    sleep(10)
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL],
        fail_silently=False,
    )
