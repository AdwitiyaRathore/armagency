from datetime import date

from django.db import models
from django.urls import reverse

# Create your models here.
    
class DataOfJob(models.Model):

    index = models.IntegerField(primary_key=True)
    jobNumber = models.IntegerField()
    noOfBooking = models.IntegerField(default=1)
    container_no = models.CharField(max_length=255)
    shippingLine = models.CharField(max_length=255)
    Forwarder = models.CharField(max_length=255)
    bookingNum = models.CharField(max_length=255)
    exporterName = models.CharField(max_length=255)
    exporterAddress = models.CharField(max_length=255)
    size_20 = models.BooleanField('size=20', default=False)
    size_40 = models.BooleanField('size=40', default=False)
    tues_1 = models.IntegerField(default=0)
    tues_2 = models.IntegerField(default=0)
    totalTues_1 = models.IntegerField(default=0)
    totalTues_2 = models.IntegerField(default=0)
    todayDate = models.DateField(default=date.today)
    
    def save(self, *args, **kwargs):

        self.tues_1 = 0
        self.tues_2 = 0

        # Set values based on size_20 and size_40
        if self.size_20 and self.size_40:
            self.tues_1, self.tues_2 = 1, 2
        elif self.size_40:
            self.tues_2 = 2
        elif self.size_20:
            self.tues_1 = 1

        # Call the parent class save method
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("jobData:jobList")
    
    def __str__(self):
        return str(self.index)