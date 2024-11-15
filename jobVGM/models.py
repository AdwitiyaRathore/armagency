from datetime import date

from django.db import models
from django.urls import reverse
from jobData.models import DataOfJob

# Create your models here.

class VgmModel(models.Model):

    PERMISSIBLE_WEIGHT_CHOICES = [
        (32500, '32,500 lbs'),
        (32450, '32,450 lbs'),
    ]

    index = models.ForeignKey(DataOfJob, on_delete=models.CASCADE, primary_key=True)
    jobNumber = models.IntegerField(blank=True, null=True)
    exporterName = models.CharField(max_length=255, blank=True)
    exporterAddress = models.CharField(max_length=255, blank=True)
    IEC_no = models.IntegerField(blank=True, null=True)
    NameOfAuthorised = models.CharField(max_length=255, blank=True)
    bookingNum = models.CharField(max_length=255, blank=True)
    DesignationOfAuthorised = models.CharField(max_length=255, blank=True)
    contactDetail = models.IntegerField(blank=True, null=True)
    containerNum = models.CharField(max_length=255, blank=True)
    size_20 = models.BooleanField('size=20', default=False)
    size_40 = models.BooleanField('size=40', default=False)
    permissibleWeight = models.IntegerField(blank=True, null=True, choices=PERMISSIBLE_WEIGHT_CHOICES)
    WeighBridgeRegistration = models.CharField(max_length=255, blank=True)
    WeighBridgeAddress = models.CharField(max_length=255, blank=True)
    emptyContainerMass = models.FloatField(blank=True, null=True)
    goodMass = models.FloatField(blank=True, null=True)
    dateOfWeigh = models.DateField(blank=True, null=True)
    timeofWeigh = models.TimeField(blank=True, null=True)
    cargoWeight = models.IntegerField(blank=True, null=True)
    containerWeight = models.IntegerField(blank=True, null=True)
    verifiedGrossMass = models.FloatField(blank=True, null=True)
    weightmentSlipNum = models.CharField(max_length=255, blank=True)
    unitOfMeasure = models.CharField(max_length=255, blank=True)
    typeOF = models.CharField(max_length=255, default='NA', blank=True)
    ifHazardous = models.CharField(max_length=255, default='NA', blank=True)
    signatureImg = models.ImageField(upload_to='signature_pic/%y', blank=True, null=True)
    todayDate = models.DateField(default=date.today)
    vesselName = models.CharField(max_length=255, blank=True, null=True, default='NA')
    vcnNo = models.CharField(max_length=255, blank=True, null=True, default='NA')

    def save(self, *args, **kwargs):
        if self.cargoWeight is not None and self.containerWeight is not None:
            self.verifiedGrossMass = self.cargoWeight + self.containerWeight
        else:
            self.verifiedGrossMass = None

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.index)
    
    def get_absolute_url(self):
        return reverse('jobVGM:vgmDetail', kwargs={'pk': self.pk})
