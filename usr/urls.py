from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_inputs, name='user-birthdate'),
    path('result/', views.calculator, name='result-page')
]