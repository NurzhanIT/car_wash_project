from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.viewsets import ModelViewSet

from .models import VideoSet, VideoFile, Car
from .serializers import VideoSetSerializer, VideoSerializer, CarSerializer


class VideoSetView(generics.ListAPIView):
    queryset = VideoSet.objects.all()
    serializer_class = VideoSetSerializer



class VideoFileView(generics.ListAPIView):
    queryset = VideoFile.objects.all()
    serializer_class = VideoSerializer

class CarView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer