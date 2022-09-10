from django.contrib import admin

# Register your models here.
from .models import Driver, Passenger, Ride
admin.site.register([Driver, Ride, Passenger])
