# Generated by Django 3.2.7 on 2022-11-21 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_alter_car_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.video'),
        ),
    ]