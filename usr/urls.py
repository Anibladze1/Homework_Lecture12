from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_inputs, name='user-birthdate'),
    path('result/', views.calculate_age, name='result-page')
]