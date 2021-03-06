# Generated by Django 4.0.5 on 2022-06-16 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_app', '0002_customer_car_number_customer_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='car_number',
        ),
        migrations.AddField(
            model_name='driver',
            name='car_number',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='phone_number',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='surname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taxi_app.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='update_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
