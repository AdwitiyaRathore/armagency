from datetime import date

from django.db import models
from django.urls import reverse
from jobData.models import DataOfJob

# Create your models here.

class StuffingSheetModel(models.Model):

    STUFFING_TYPE_CHOICES = [
    ('ICD STUFFING', 'ICD STUFFING'),
    ('FACTORY STUFFING', 'FACTORY '),
    ]

    DEPOT_TYPE_CHOICES = [
    ('THAR DRY PORT', 'THAR DRY PORT'),
    ('INLAND CONTAINER DEPOT', 'INLAND CONTAINER DEPOT'),
    ]


    DEPOT_ADDRESS_CHOICES = [
        ('A UNIT OF CONTAINER OF INDIA LTD BHAGAT KI KOTHI, JODHPUR', 'A UNIT OF CONTAINER OF INDIA LTD BHAGAT KI KOTHI, JODHPUR'),
        ('A UNIT OF HASTI PETRO CHEMICAL & SHIPPING LTD', 'A UNIT OF HASTI PETRO CHEMICAL & SHIPPING LTD'),
    ]

    index = models.ForeignKey(DataOfJob, on_delete=models.CASCADE, primary_key=True)
    jobNumber = models.IntegerField(blank=True, null=True)
    depot = models.CharField(max_length=255, blank=True, null=True, choices=DEPOT_TYPE_CHOICES)
    depotAddress = models.CharField(max_length=255, blank=True, null=True, choices=DEPOT_ADDRESS_CHOICES)
    stuffingType = models.CharField(max_length=255, blank=True, null=True, choices=STUFFING_TYPE_CHOICES)
    bookingNum = models.CharField(blank=True, null=True, max_length=255)
    invoiceNo = models.CharField(blank=True, null=True, max_length=255)
    containerNum = models.CharField(blank=True, null=True, max_length=255)
    shutout = models.IntegerField(blank=True, null=True)
    dateOfStuffing = models.DateField(default=date.today, blank=True, null=True)
    shippingLine = models.CharField(blank=True, null=True, max_length=255)
    customSeal = models.IntegerField(blank=True, null=True)
    size_20 = models.BooleanField('size=20', default=False)
    size_40 = models.BooleanField('size=40', default=False)
    portOfDestination = models.CharField(blank=True, null=True, max_length=255)
    shippingLineSeal = models.CharField(blank=True, null=True, max_length=255)
    portOfLoading = models.CharField(blank=True, null=True, max_length=255)
    shippingBillNo = models.IntegerField(blank=True, null=True)
    shippingBillDate = models.DateField(blank=True, null=True)
    exporterName = models.CharField(blank=True, null=True, max_length=255)
    nameOfGood = models.CharField(blank=True, null=True, max_length=255)
    noOfPkgs = models.IntegerField(blank=True, null=True)
    grossWt = models.FloatField(blank=True, null=True)
    valueINR = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.index)

    def get_absolute_url(self):
        return reverse('stuffingSheet:stuffingSheetList')
    

class TotalStuffingValue(models.Model):
    bookingNum = models.CharField(default='', blank=True, null=True, max_length=255)
    totalPkg = models.IntegerField(blank=True, null=True, default = 0)
    totalGrossWt = models.FloatField(blank=True, null=True, default = 0)
    totalvalueINR = models.FloatField(blank=True, null=True, default = 0)
