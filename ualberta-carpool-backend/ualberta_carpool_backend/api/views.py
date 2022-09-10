from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DriverSerializer
from .models import Driver

class DriverView(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
