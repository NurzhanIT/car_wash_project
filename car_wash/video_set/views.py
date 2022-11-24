from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.viewsets import ModelViewSet

from .models import VideoSet, VideoFile
from .serializers import VideoSetSerializer, VideoSerializer


class VideoSetView(generics.ListCreateAPIView):
    queryset = VideoSet.objects.all()
    serializer_class = VideoSetSerializer

    def perform_create(self, serializer):
        serializer.save()


class VideoFileView(generics.ListAPIView):
    queryset = VideoFile.objects.all()
    serializer_class = VideoSerializer

    # def get_queryset(self):
    #     video_set = VideoSet.objects.all()
    #     return VideoFile.objects.filter(video_set=video_set)
    #
    #
