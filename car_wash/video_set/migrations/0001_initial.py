# Generated by Django 3.2.7 on 2022-11-27 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('come_time', models.DateTimeField()),
                ('left_time', models.DateTimeField()),
                ('car_brand', models.TextField(max_length=100)),
                ('car_type', models.TextField(max_length=100)),
                ('car_nomer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VideoFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video/videos/')),
                ('quantity_of_cars', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VideoSet',
            fields=[
                ('set_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('set_date', models.DateField(blank=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='videoset',
            constraint=models.UniqueConstraint(fields=('set_name',), name='unique_video_set_by_user'),
        ),
        migrations.AddField(
            model_name='videofile',
            name='video_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video_set.videoset'),
        ),
        migrations.AddField(
            model_name='car',
            name='related_video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video_set.videofile'),
        ),
    ]
