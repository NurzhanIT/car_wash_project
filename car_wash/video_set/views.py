from rest_framework import generics
from .models import VideoSet, VideoFile, Frame
from .serializers import VideoSetSerializer, VideoSerializer, FramesSerializer


class VideoSetView(generics.ListAPIView):
    queryset = VideoSet.objects.all()
    serializer_class = VideoSetSerializer


class VideoFileView(generics.ListAPIView):
    queryset = VideoFile.objects.all()
    serializer_class = VideoSerializer


class FramesView(generics.ListCreateAPIView):
    queryset = Frame.objects.all()
    serializer_class = FramesSerializer