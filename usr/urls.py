from django.urls import path
from . import views


urlpatterns = [
    path('', views.calculation, name='user-birthdate')
]