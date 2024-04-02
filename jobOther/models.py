from django.db import models
from jobData.models import DataOfJob
from django.urls import reverse

# Create your models here.
class OtherModel(models.Model):

    CONTAINER_METHOD_TYPE = [
        ('1', 'Method-1'), 
        ('2', 'Method-2'),
    ]

    jobNumber = models.OneToOneField(DataOfJob, primary_key=True, on_delete=models.CASCADE)
    bookingNum = models.CharField(default='', blank=True, null=True, max_length=255)
    containerNum = models.CharField(max_length=255, blank=True)
    doExpityDate = models.DateField(blank=True, null=True)
    dispatchDate = models.DateField(blank=True, null=True)
    invoiceDate = models.DateField(blank=True, null=True)
    containerMethodType = models.CharField(default='', max_length=255, blank=True, null=True, choices=CONTAINER_METHOD_TYPE)
    PanNo = models.CharField(default='', max_length=255, blank=True, null=True)
    vessealCutOffDate = models.DateField(blank=True, null=True)
    handoverDate = models.DateField(blank=True, null=True)
    allotmentDate = models.DateField(blank=True, null=True)
    ChaName = models.CharField(default='', blank=True, null=True, max_length=255)
    seaPortInDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.bookingNum
    
    def get_absolute_url(self):
        return reverse('jobOther:jobOtherList')