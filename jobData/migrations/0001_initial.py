# Generated by Django 4.2.8 on 2024-04-02 09:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DataOfJob",
            fields=[
                ("jobNumber", models.IntegerField(primary_key=True, serialize=False)),
                ("noOfBooking", models.IntegerField(default=1)),
                ("shippingLine", models.CharField(max_length=255)),
                ("Forwarder", models.CharField(max_length=255)),
                ("bookingNum", models.CharField(max_length=255)),
                ("exporterName", models.CharField(max_length=255)),
                ("exporterAddress", models.CharField(max_length=255)),
                ("size_20", models.BooleanField(default=False, verbose_name="size=20")),
                ("size_40", models.BooleanField(default=False, verbose_name="size=40")),
                ("tues_1", models.IntegerField(default=0)),
                ("tues_2", models.IntegerField(default=0)),
                ("totalTues_1", models.IntegerField(default=0)),
                ("totalTues_2", models.IntegerField(default=0)),
                ("todayDate", models.DateField(default=datetime.date.today)),
            ],
        ),
    ]