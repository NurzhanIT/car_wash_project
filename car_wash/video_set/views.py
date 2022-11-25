from rest_framework import generics
from .models import VideoSet, VideoFile
from .serializers import VideoSetSerializer, VideoSerializer


class VideoSetView(generics.ListAPIView):
    queryset = VideoSet.objects.all()
    serializer_class = VideoSetSerializer


class VideoFileView(generics.ListAPIView):
    queryset = VideoFile.objects.all()
    serializer_class = VideoSerializer
