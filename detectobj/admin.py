from django.contrib import admin
from .models import DetectedObj


@admin.register(DetectedObj)
class DetectedObjAdmin(admin.ModelAdmin):
    list_display = ["original_video"]