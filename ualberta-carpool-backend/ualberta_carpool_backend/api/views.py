from tabnanny import check
from math import sin, cos, radians, acos
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import DriverSerializer, PassengerSerializer, RideSerializer
from .models import Driver, Passenger, Ride


EARTH_RADIUS_IN_MILES = 3958.761

class DriverView(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

class PassengerView(viewsets.ModelViewSet):
    serializer_class = PassengerSerializer
    queryset = Passenger.objects.all()

    # def create(self, request, *args, **kwargs):
    #     pass_data = request.data
    
    #     ride_data = Ride.objects.get(id=pass_data["ride"])
        
    #     if (ride_data.capacity > ride_data.passengers.all().count()):
    #         new_passenger = Passenger.objects.create(
    #             name=pass_data["name"], phone_number=pass_data["phone_number"], ride=ride_data)
    #         new_passenger.save()

    #         serializer = PassengerSerializer(new_passenger)
    #         return HttpResponse(serializer.data)

    #     return HttpResponse("Failed to add passenger to carpool")

class RideView(viewsets.ModelViewSet):    
    serializer_class = RideSerializer
    queries = Ride.objects.all()
    ride_list = []

    for q in queries:
        current_passengers = q.passengers.all().count() + 1
        if (current_passengers < q.capacity):
            ride_list.append(q)

    queryset = Ride.objects.filter(driver__name__in=ride_list)