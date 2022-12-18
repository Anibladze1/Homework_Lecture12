# from django.conf import settings
from django.db import models
# from django.utils import timezone
# import datetime


class User(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)

    # def calculator(self):
    #     return int((datetime.date.year - self.birth_date.year) + 1)
    #
    # age = property(calculator)
