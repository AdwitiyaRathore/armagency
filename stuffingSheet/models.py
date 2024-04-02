from django.db import models
from jobData.models import DataOfJob
from datetime import date
from django.urls import reverse
# Create your models here.

class StuffingSheetModel(models.Model):

    STUFFING_TYPE_CHOICES = [
    ('ICD', 'ICD Stuffing'),
    ('Factory', 'Factory Stuffing'),
    ]

    DEPOT_TYPE_CHOICES = [
        ('Thar', 'THAR DRY PORT'),
        ('Inland', 'INLAND CONTAINER DEPOT'),
    ]

    DEPOT_ADDRESS_CHOICES = [
        ('ContainerIndia', 'A UNIT OF CONTAINER OF INDIA LTD BHAGAT KI KOTHI, JODHPUR'),
        ('Hasti', 'A UNIT OF HASTI PETRO CHEMICAL & SHIPPING LTD'),
    ]

    jobNumber = models.OneToOneField(DataOfJob, primary_key=True, on_delete=models.CASCADE)
    depot = models.CharField(default='Thar', max_length=255, blank=True, null=True, choices=DEPOT_TYPE_CHOICES)
    depotAddress = models.CharField(default="A UNIT OF HASTI PETRO CHEMICAL & SHIPPING LTD', 'Hasti'", max_length=255, blank=True, null=True, choices=DEPOT_ADDRESS_CHOICES)
    stuffingType = models.CharField(default='ICD Stuffing', max_length=255, blank=True, null=True, choices=STUFFING_TYPE_CHOICES)
    bookingNum = models.CharField(default='', blank=True, null=True, max_length=255)
    invoiceNo = models.CharField(default='', blank=True, null=True, max_length=255)
    containerNum = models.CharField(default='', blank=True, null=True, max_length=255)
    shutout = models.IntegerField(default=0, blank=True, null=True)
    dateOfStuffing = models.DateField(default=date.today, blank=True, null=True)
    shippingLine = models.CharField(default='', blank=True, null=True, max_length=255)
    customSeal = models.IntegerField(default=0, blank=True, null=True)
    size_20 = models.BooleanField('size=20', default=False)
    size_40 = models.BooleanField('size=40', default=False)
    portOfDestination = models.CharField(default='', blank=True, null=True, max_length=255)
    shippingLineSeal = models.CharField(default='', blank=True, null=True, max_length=255)
    portOfLoading = models.CharField(default='', blank=True, null=True, max_length=255)
    shippingBillNo = models.IntegerField(default=0, blank=True, null=True)
    shippingBillDate = models.DateField(default=date.today, blank=True, null=True)
    exporterName = models.CharField(default='', blank=True, null=True, max_length=255)
    nameOfGood = models.CharField(default='', blank=True, null=True, max_length=255)
    noOfPkgs = models.IntegerField(default=0, blank=True, null=True)
    grossWt = models.FloatField(default=0.0, blank=True, null=True)
    valueINR = models.FloatField(default=0.0, blank=True, null=True)

    def __str__(self):
        return self.exporterName

    def get_absolute_url(self):
        return reverse('stuffingSheet:stuffingSheetList')
    

class TotalStuffingValue(models.Model):
    bookingNum = models.CharField(default='', blank=True, null=True, max_length=255)
    totalPkg = models.IntegerField(blank=True, null=True, default = 0)
    totalGrossWt = models.FloatField(blank=True, null=True, default = 0)
    totalvalueINR = models.FloatField(blank=True, null=True, default = 0)
