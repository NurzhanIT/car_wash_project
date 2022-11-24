from django.db import models
import torchvision
import torch


# class Video(models.Model):
#     video = models.FileField(upload_to='video/videos/', primary_key=True)
#     date = models.DateField(auto_now_add=False)
#     carNum = models.IntegerField()
#
#
# class Car(models.Model):
#     date = models.DateField(auto_now_add=False)
#     arrived_time = models.TimeField()
#     left_time = models.TimeField()
#     video = models.ForeignKey(Video, on_delete=models.CASCADE)
#     id = models.IntegerField(max_length=1000)


class VideoSet(models.Model):
    name = models.TextField(max_length=100, primary_key=True)
    video = models.FileField(upload_to='video/videos/')
    video_date = models.DateField(auto_now_add=False, blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['name', 'video_date'],
            name='unique_videoset_by_user')]


class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    car_brand = models.TextField(max_length=100)
    car_type = models.TextField(max_length=100)
    car_nomer = models.CharField(max_length=100)
    quantity_of_cars = models.IntegerField()
    video = models.ForeignKey(VideoSet, on_delete=models.CASCADE)
