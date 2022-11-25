from django.db import models


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

# !User создает VideoSet. Сет имеет видеоматериалы(VideoFiles) за определенный интервал времени.
#
class VideoSet(models.Model):
    set_name = models.CharField(max_length=100, primary_key=True)
    set_start_date = models.DateField(auto_now_add=False, blank=True)
    set_end_date = models.DateField(auto_now_add=False, blank=True)


    def __str__(self):
        return self.set_name

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['set_name'],
            name='unique_video_set_by_user')]


class VideoFile(models.Model):
    video = models.FileField(upload_to='video/videos/')
    video_set = models.ForeignKey('video_set.VideoSet', on_delete=models.CASCADE)


class Car(models.Model):
    come_time = models.DateTimeField(auto_now_add=False)
    left_time = models.DateTimeField(auto_now_add=False)
    car_brand = models.TextField(max_length=100)
    car_type = models.TextField(max_length=100)
    car_nomer = models.CharField(max_length=100)
    related_video = models.ForeignKey('video_set.VideoFile', on_delete=models.CASCADE)
