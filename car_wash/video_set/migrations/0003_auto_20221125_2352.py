# Generated by Django 3.2.7 on 2022-11-25 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_set', '0002_rename_video_car_related_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videoset',
            old_name='set_end_date',
            new_name='set_date',
        ),
        migrations.RemoveField(
            model_name='videoset',
            name='set_start_date',
        ),
    ]
