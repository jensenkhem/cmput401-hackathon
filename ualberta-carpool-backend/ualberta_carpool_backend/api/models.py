from unicodedata import name
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Driver(models.Model):
    name = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    desired_arrival_time = models.TimeField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.name
