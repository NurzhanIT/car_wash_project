import torch.hub
from django.db import models


class Video(models.Model):
    video = models.FileField(upload_to='video/videos/', primary_key=True)
    date = models.DateField(auto_now_add=False)
    carNum = models.IntegerField()


class Car(models.Model):
    date = models.DateField(auto_now_add=False)
    arrived_time = models.TimeField()
    left_time = models.TimeField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    id = models.IntegerField(max_length=1000)
