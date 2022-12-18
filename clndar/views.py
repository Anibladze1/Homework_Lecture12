from django.shortcuts import render
from django.http import HttpResponse
import datetime


def home(request):
    return render(request, 'clndar/home.html')


def date_today(request):
    date = datetime.date.today()
    return HttpResponse(date)
