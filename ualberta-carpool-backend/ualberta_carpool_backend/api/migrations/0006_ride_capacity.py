# Generated by Django 4.1.1 on 2022-09-11 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_passenger_ride'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='capacity',
            field=models.IntegerField(default=2),
        ),
    ]
