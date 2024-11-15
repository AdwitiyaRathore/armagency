from django import forms
from django.forms import ModelForm

from . import models


class NewData(ModelForm):

    jobNumber = forms.CharField(label='Job Number')
    noOfBooking = forms.IntegerField(label='No Of Booking')
    shippingLine = forms.CharField(label='Shipping Line')
    Forwarder = forms.CharField(label='Forwarder')
    bookingNum = forms.CharField(label='Booking No')
    exporterName = forms.CharField(label='Exporter Name')
    exporterAddress = forms.Textarea()

    class Meta:
        model = models.DataOfJob
        exclude = ['tues_1', 'tues_2', 'todayDate', 'totalTues_2', 'totalTues_1']
        widgets = {
            'size_20': forms.CheckboxInput(),
            'size_40': forms.CheckboxInput(),
            'exporterAddress': forms.Textarea(attrs={'rows': 5})
        }

    def clean(self):
        cleaned_data = super().clean()

        fields_to_uppercase = [
        'shippingLine', 'Forwarder', 'bookingNum', 'exporterName', 'exporterAddress'
        ]

        for field in fields_to_uppercase:
            if field is not None:
                cleaned_data[field] = cleaned_data.get(field, '').upper()