from django.test import TestCase
from .models import Driver, Passenger, Ride

# Create your tests here.
class DriverTestCase(TestCase):
    def setUp(self):
        Driver.objects.create(name='TestDriver', latitude=90, longitude=90, desired_arrival_time='09:00:00', phone_number='+15875914104')
    
class PassengerTestCase(TestCase):
    def setUp(self):
        Passenger.objects.create(name='TestPassenger1')