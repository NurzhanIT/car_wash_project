# Generated by Django 3.2.7 on 2022-11-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_set', '0002_remove_videofile_quantity_of_cars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frames', models.ImageField(upload_to='api_frames/frames/')),
            ],
        ),
    ]
