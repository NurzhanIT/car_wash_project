from django.db import models


# !User создает VideoSet в котором видео записи за отдельные боксы
#
class VideoSet(models.Model):
    set_name = models.CharField(max_length=100)
    set_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.set_name

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['set_name'],
            name='unique_video_set_by_user')]


class VideoFile(models.Model):
    video = models.FileField(upload_to='video/videos/')
    video_date = models.DateField(auto_now_add=False)
    video_set = models.ForeignKey('video_set.VideoSet', on_delete=models.CASCADE)
    box = models.CharField(max_length=50, default='номер бокса')


class Car(models.Model):
    come_time = models.DateTimeField(auto_now_add=False)
    left_time = models.DateTimeField(auto_now_add=False)
    car_brand = models.TextField(max_length=100)
    car_type = models.TextField(max_length=100)
    car_nomer = models.CharField(max_length=100)
    related_video = models.ForeignKey('video_set.VideoFile', on_delete=models.CASCADE)
