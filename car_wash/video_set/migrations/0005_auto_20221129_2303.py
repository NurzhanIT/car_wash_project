# Generated by Django 3.2.7 on 2022-11-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_set', '0004_auto_20221129_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frame',
            name='frame',
        ),
        migrations.AddField(
            model_name='frame',
            name='name',
            field=models.CharField(default='name', max_length=100),
            preserve_default=False,
        ),
    ]
