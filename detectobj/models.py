from django.db import models
from config.models import CreationModificationDateBase


class DetectedObj(CreationModificationDateBase):
    original_video = models.ForeignKey(
        "video.VideoFile",
        on_delete=models.CASCADE,
        related_name="detectedvideos",
        help_text="Main Video",
        null=True,
        blank=True
    )
