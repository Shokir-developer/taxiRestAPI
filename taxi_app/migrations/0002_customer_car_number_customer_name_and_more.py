# Generated by Django 4.0.5 on 2022-06-16 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='car_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='surname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]