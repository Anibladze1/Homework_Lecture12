# from django.conf import settings
import datetime

from django.db import models


# from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)

    @property
    def calculate_age(self):
        if self.birth_date:
            today = datetime.date.today()
            return today.year - self.birth_date.year - (
                        (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return 0

