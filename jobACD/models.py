from datetime import date

from django.db import models
from django.urls import reverse
from jobData.models import DataOfJob

# Create your models here.

class AcdModel(models.Model):

    index = models.ForeignKey(DataOfJob, on_delete=models.CASCADE, primary_key=True)
    jobNumber = models.IntegerField(blank=True, null=True, default=0)
    exporterAddress = models.CharField(default='Exporter Address', blank=True, null=True, max_length=255)
    bookingNum = models.CharField(default='Booking Num', blank=True, null=True, max_length=255)
    consignee = models.CharField(default='Consignee', blank=True, null=True, max_length=255)
    nameOfOceanCarrier = models.CharField(default='Name Of Ocean Carrier', blank=True, null=True, max_length=255)
    vesselName = models.CharField(default='Vessel Name', blank=True, null=True, max_length=255)
    placeOfReceiptOfGood = models.CharField(default='Place Of Receipt Of Good', blank=True, null=True, max_length=255)
    portOfLoading = models.CharField(default='Port Of Loading', blank=True, null=True, max_length=255)
    portOfDischarge = models.CharField(default='Port Of Discharge', blank=True, null=True, max_length=255)
    placeOfDeliveryWithStateCode = models.CharField(default='Place Of Delivery', blank=True, null=True, max_length=255)
    containerNum = models.CharField(default='Container Num', blank=True, null=True, max_length=255)
    customSeal = models.IntegerField(default=0, blank=True, null=True, max_length=255)
    shippingBillNo = models.IntegerField(default=0, blank=True, null=True)
    marks = models.CharField(default='Marks', blank=True, null=True, max_length=255)
    noOfPkgs = models.IntegerField(default=0, blank=True, null=True)
    fullCommondityDescription = models.CharField(default='Description', max_length=255, blank=True, null=True)
    grossWt = models.FloatField(default=0.0, blank=True, null=True)
    htsCode = models.IntegerField(default=0, blank=True, null=True)
    placeOfIssueOfCargo = models.CharField(default='Issue Of Cargo', max_length=255, blank=True, null=True)
    dateOfIssueOfCargo = models.DateField(default=date.today, blank=True, null=True)
    exporterName = models.CharField(default='Exporter Name', blank=True, null=True, max_length=255)
    NameOfAuthorised = models.CharField(default='Name Of Authorised', max_length=255, blank=True)
    signatureImg = models.ImageField(upload_to='signature_pic/%y', blank=True, null=True)

    def __str__(self):
        return str(self.index)
    
    def get_absolute_url(self):
        return reverse('jobACD:acdDetail', kwargs={'pk': self.pk})