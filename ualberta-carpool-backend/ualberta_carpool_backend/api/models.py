from lib2to3.pgen2 import driver
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Driver(models.Model):
    name = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    desired_arrival_time = models.TimeField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

class Ride(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    capacity = models.IntegerField(default=2)
    
    def __str__(self):
        return self.driver.name

class Passenger(models.Model):
    name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    ride = models.ForeignKey('Ride', on_delete=models.CASCADE, blank=True, null=True, related_name='passengers')
    
    def __str__(self):
        return self.name

 
