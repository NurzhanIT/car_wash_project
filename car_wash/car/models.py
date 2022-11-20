from django.db import models


class Video(models.Model):
    video = models.FileField(upload_to='uploads/')
    date = models.DateTimeField(auto_now=False)
    carNum = models.IntegerField(max_length=200)


def __str__(self):
    return self.body[0:50]
