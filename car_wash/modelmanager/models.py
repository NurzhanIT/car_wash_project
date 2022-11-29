import os
import yaml

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.urls import reverse

from config.models import CreationModificationDateBase

User = settings.AUTH_USER_MODEL


def model_upload_path(instance, filename):
    return f'{instance.uploader.username}/ml_models/{instance.name}/{filename}'


class MLModel(CreationModificationDateBase):
    uploader = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='mlmodels'
                                 )

    name = models.CharField(_('Name'),
                            max_length=100,
                            help_text='Name for the ml model'
                            )

    pth_file = models.FileField(_('Upload Model Pt/Pth File'),
                                upload_to=model_upload_path,
                                validators=[FileExtensionValidator(
                                    allowed_extensions=['pt', 'pth']
                                )],
                                help_text='Allowed extensions are: .pt, .pth'
                                )

    description = models.TextField(_("Model's description"))

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=('name', 'uploader'),
            name='unique_model_by_user'
        )]
