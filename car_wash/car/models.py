from django.db import models


class Video(models.Model):
    video = models.FileField(upload_to='video/videos/')
    date = models.DateField(auto_now_add=False)
    carNum = models.IntegerField()


    # def __str__(self):
    #     return self.body[0:50]


class Car(models.Model):

    date = models.DateField(auto_now_add=False)
    arrived_time = models.TimeField()
    left_time = models.TimeField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE)