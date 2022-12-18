from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "birth_date"]
        labels = {"name": "Name", "birth_date": "Birthdate (Y-MM-DD)"}

