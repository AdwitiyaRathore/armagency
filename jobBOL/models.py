from django.db import models
from django.urls import reverse
from jobData.models import DataOfJob

# Create your models here.

class BolModel(models.Model):

    index = models.ForeignKey(DataOfJob, on_delete=models.CASCADE, primary_key=True)
    jobNumber = models.IntegerField(blank=True, null=True)
    exporterName = models.CharField(blank=True, null=True, max_length=255)
    exporterAddress = models.CharField(max_length=255, blank=True)
    gstin = models.CharField(blank=True, null=True, max_length=255)
    consignee = models.CharField(blank=True, null=True, max_length=255)
    notifyDelivery = models.CharField(blank=True, null=True, max_length=255)
    bookingNum = models.CharField(blank=True, null=True, max_length=255)
    shippingLine = models.CharField(blank=True, null=True, max_length=255)
    armAddress = models.CharField(blank=True, null=True, max_length=255, default='48, District Shopping Center underground Saraswati Nagar, Pali Road, Jodhpur')
    initialCarriage_mode = models.CharField(blank=True, null=True, max_length=255)
    placeOfReceiptOfGood = models.CharField(blank=True, null=True, max_length=255)
    vesselName = models.CharField(blank=True, null=True, max_length=255)
    portOfLoading = models.CharField(blank=True, null=True, max_length=255)
    portOfDestination = models.CharField(blank=True, null=True, max_length=255)
    finalDestination = models.CharField(blank=True, null=True, max_length=255)
    marks = models.CharField(max_length=255, blank=True, null=True)
    noOfPkgs = models.IntegerField(blank=True, null=True)
    grossWt = models.FloatField(blank=True, null=True)
    netWt = models.FloatField(blank=True, null=True)
    CBM = models.FloatField(blank=True, null=True)
    descriptionOfGood = models.CharField(blank=True, null=True, max_length=255)
    shippingBillNo = models.IntegerField(blank=True, null=True)
    IECno = models.IntegerField(blank=True, null=True)
    invoiceNo = models.CharField(blank=True, null=True, max_length=255)
    hsCode = models.CharField(blank=True, null=True, max_length=255)
    poCode = models.CharField(blank=True, null=True, max_length=255)
    containerNum = models.CharField(blank=True, null=True, max_length=255)
    shippingLineSeal = models.CharField(blank=True, null=True, max_length=255)
    customSeal = models.IntegerField(blank=True, null=True)
    freight = models.CharField(blank=True, null=True, max_length=255)
    dateOfIssue = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.index)

    def get_absolute_url(self):
        return reverse('jobBOL:bolDetail', kwargs={'pk': self.pk})