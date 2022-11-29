from django.db import models
from django.config.models import CreationModificationDateBase


class InferencedFrame(CreationModificationDateBase):
    original_video = models.ForeignKey(
        "video_set.VideoFile",
        on_delete=models.CASCADE,
        related_name="detectedframe",
        help_text="Main frame",
        null=True,
        blank=True
    )
    detection_info = models.JSONField(null=True, blank=True)
