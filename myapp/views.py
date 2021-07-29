from django.shortcuts import render
from django.http import HttpResponse

from .tasks import add, send_email


def index(request):
    response = add.delay(10, 10)
    print(response.ready())
    return HttpResponse(f"Answer is {response}")


def send_message(request):
    send_email.apply_async(("ruslaneleusinov@gmail.com",), countdown=10)
    return HttpResponse("Was sent")
