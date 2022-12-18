from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("datetoday/", views.date_today, name = "date-today"),
]