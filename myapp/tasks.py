from django.conf import settings
from django.core.mail import send_mail

from MQ.celery import app


@app.task
def add(x, y):
    return x + y


@app.task
def send_email(user_email: str) -> None:
    send_mail("Hello, man!", "Be strong!", settings.EMAIL_HOST_USER, [user_email])
