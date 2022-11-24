from django.db import models
from django.config.models import CreationModificationDateBase


class DetectedObj(CreationModificationDateBase):
    original_video = models.ForeignKey(
        "video_set.VideoFile",
        on_delete=models.CASCADE,
        related_name="detectedvideos",
        help_text="Main Video",
        null=True,
        blank=True
    )
