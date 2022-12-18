from django.shortcuts import render
import datetime
from .models import User
from django.http import HttpResponse


def calculation(request):
    user = User
    date_today = datetime.date.today()

    return HttpResponse(user.birth_date)
    # return render(request, 'usr/user.html')
