from django.shortcuts import render
from .tasks import add_data
from django.http import HttpResponse

def test(request):
    add_data.delay(6,5)
    return HttpResponse("Happy")