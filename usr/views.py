from django.shortcuts import render, redirect
import datetime
from .models import User
from django.http import HttpResponse
from .forms import UserForm


def user_inputs(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result-page')

    else:
        form = UserForm()

    return render(request, 'usr/user.html', {'form': form})


def calculator(request):
    # age = User().age
    return HttpResponse(User())
