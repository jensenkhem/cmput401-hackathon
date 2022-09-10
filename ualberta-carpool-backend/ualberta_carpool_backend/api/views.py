from tabnanny import check
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DriverSerializer, PassengerSerializer, RideSerializer
from .models import Driver, Passenger, Ride

class DriverView(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

class PassengerView(viewsets.ModelViewSet):
    serializer_class = PassengerSerializer
    queryset = Passenger.objects.all()

class RideView(viewsets.ModelViewSet):
    serializer_class = RideSerializer
    queryset = Ride.objects.all()

