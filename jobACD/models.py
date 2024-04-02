from django.db import models
from jobData.models import DataOfJob
from django.urls import reverse

# Create your models here.

class AcdModel(models.Model):

    jobNumber = models.OneToOneField(DataOfJob, primary_key=True, on_delete=models.CASCADE)
    bookingNum = models.CharField(blank=True, null=True, max_length=255)
    exporterAddress = models.CharField(blank=True, null=True, max_length=255)
    consignee = models.CharField(blank=True, null=True, max_length=255)
    nameOfOceanCarrier = models.CharField(blank=True, null=True, max_length=255)
    vesselName = models.CharField(blank=True, null=True, max_length=255)
    placeOfReceiptOfGood = models.CharField(blank=True, null=True, max_length=255)
    portOfLoading = models.CharField(blank=True, null=True, max_length=255)
    portOfDischarge = models.CharField(blank=True, null=True, max_length=255)
    placeOfDeliveryWithStateCode = models.CharField(blank=True, null=True, max_length=255)
    containerNum = models.CharField(blank=True, null=True, max_length=255)
    customSeal = models.CharField(blank=True, null=True, max_length=255)
    shippingBillNo = models.IntegerField(blank=True, null=True)
    marks = models.CharField(blank=True, null=True, max_length=255)
    noOfPkgs = models.IntegerField(blank=True, null=True)
    fullCommondityDescription = models.CharField(max_length=255, blank=True, null=True)
    grossWt = models.FloatField(blank=True, null=True)
    htsCode = models.IntegerField(blank=True, null=True)
    placeOfIssueOfCargo = models.CharField(max_length=255, blank=True, null=True)
    dateOfIssueOfCargo = models.DateField(blank=True, null=True)
    exporterName = models.CharField(blank=True, null=True, max_length=255)
    NameOfAuthorised = models.CharField(max_length=255, blank=True)
    signatureImg = models.ImageField(upload_to='signature_pic/%y', blank=True, null=True)

    def __str__(self):
        return self.exporterName

    def get_absolute_url(self):
        return reverse('jobACD:acdDetail', kwargs={'pk': self.pk})        