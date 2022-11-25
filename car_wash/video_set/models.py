from django.db import models


# !User создает VideoSet в котором видео записи за отдельные боксы
#
class VideoSet(models.Model):
    set_name = models.CharField(max_length=100, primary_key=True)
    set_date = models.DateField(auto_now_add=False, blank=True)

    def __str__(self):
        return self.set_name

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['set_name'],
            name='unique_video_set_by_user')]


class VideoFile(models.Model):
    video = models.FileField(upload_to='video/videos/')
    video_set = models.ForeignKey('video_set.VideoSet', on_delete=models.CASCADE)
    quantity_of_cars = models.IntegerField()


