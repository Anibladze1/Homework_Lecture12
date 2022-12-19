from django.db import models
import datetime


# from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.IntegerField(null=True)

    # def calculate_age(self):
    #     return int((datetime.datetime.now().year - int(self.birth_date) +1))
    #
    # age = property(calculate_age)

    def __str__(self):
        return self.name
