# Generated by Django 5.1.1 on 2024-11-01 11:34

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("jobData", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AcdModel",
            fields=[
                (
                    "index",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="jobData.dataofjob",
                    ),
                ),
                ("jobNumber", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "exporterAddress",
                    models.CharField(
                        blank=True,
                        default="Exporter Address",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "bookingNum",
                    models.CharField(
                        blank=True, default="Booking Num", max_length=255, null=True
                    ),
                ),
                (
                    "consignee",
                    models.CharField(
                        blank=True, default="Consignee", max_length=255, null=True
                    ),
                ),
                (
                    "nameOfOceanCarrier",
                    models.CharField(
                        blank=True,
                        default="Name Of Ocean Carrier",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "vesselName",
                    models.CharField(
                        blank=True, default="Vessel Name", max_length=255, null=True
                    ),
                ),
                (
                    "placeOfReceiptOfGood",
                    models.CharField(
                        blank=True,
                        default="Place Of Receipt Of Good",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "portOfLoading",
                    models.CharField(
                        blank=True, default="Port Of Loading", max_length=255, null=True
                    ),
                ),
                (
                    "portOfDischarge",
                    models.CharField(
                        blank=True,
                        default="Port Of Discharge",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "placeOfDeliveryWithStateCode",
                    models.CharField(
                        blank=True,
                        default="Place Of Delivery",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "containerNum",
                    models.CharField(
                        blank=True, default="Container Num", max_length=255, null=True
                    ),
                ),
                (
                    "customSeal",
                    models.IntegerField(
                        blank=True, default=0, max_length=255, null=True
                    ),
                ),
                (
                    "shippingBillNo",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                (
                    "marks",
                    models.CharField(
                        blank=True, default="Marks", max_length=255, null=True
                    ),
                ),
                ("noOfPkgs", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "fullCommondityDescription",
                    models.CharField(
                        blank=True, default="Description", max_length=255, null=True
                    ),
                ),
                ("grossWt", models.FloatField(blank=True, default=0.0, null=True)),
                ("htsCode", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "placeOfIssueOfCargo",
                    models.CharField(
                        blank=True, default="Issue Of Cargo", max_length=255, null=True
                    ),
                ),
                (
                    "dateOfIssueOfCargo",
                    models.DateField(
                        blank=True, default=datetime.date.today, null=True
                    ),
                ),
                (
                    "exporterName",
                    models.CharField(
                        blank=True, default="Exporter Name", max_length=255, null=True
                    ),
                ),
                (
                    "NameOfAuthorised",
                    models.CharField(
                        blank=True, default="Name Of Authorised", max_length=255
                    ),
                ),
                (
                    "signatureImg",
                    models.ImageField(
                        blank=True, null=True, upload_to="signature_pic/%y"
                    ),
                ),
            ],
        ),
    ]
