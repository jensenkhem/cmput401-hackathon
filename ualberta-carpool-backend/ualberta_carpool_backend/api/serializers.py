from rest_framework import serializers
from .models import Driver, Passenger, Ride

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"
    
    def validate(self, data):
        ride = Ride.objects.get(id=data['ride'].id)
        ride_passenger_count = ride.passengers.all().count()
        if ride_passenger_count + 1 >= ride.capacity:
           raise serializers.ValidationError("ride is at max capacity")
        return data 
        
class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = "__all__"