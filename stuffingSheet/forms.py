from django.forms import ModelForm
from django import forms
from .models import StuffingSheetModel, TotalStuffingValue


class StuffingSheetForm(ModelForm):

    ## Field Custom Name....
    jobNumber = forms.IntegerField(required=False, label='Job Number')
    bookingNum = forms.CharField(required=False, label='Booking Num')
    invoiceNo = forms.CharField(required=False, label='Invoice No')
    containerNum = forms.CharField(required=False, label='Container Num')
    shutout = forms.IntegerField(required=False, label='Shutout')
    shippingLine = forms.CharField(required=False, label='Shipping Line')
    customSeal = forms.IntegerField(required=False, label='Custom Seal')
    portOfDestination = forms.CharField(required=False, label='Port Of Destination')
    shippingLineSeal = forms.CharField(required=False, label='Shipping Line Seal')
    portOfLoading = forms.CharField(required=False, label='Port Of Loading')
    exporterName = forms.CharField(required=False, label='Exporter Name')
    shippingBillNo = forms.IntegerField(required=False, label='Shipping Bill No')
    nameOfGood = forms.CharField(required=False, label='Name Of Good')
    noOfPkgs = forms.IntegerField(required=False, label='No Of Pkgs')
    grossWt = forms.FloatField(required=False, label='Gross Wt')
    valueINR = forms.FloatField(required=False, label='Value INR')

    class Meta():
        model = StuffingSheetModel
        exclude = ['tues_1', 'tues_2', 'totalPkg', 'totalGrossWt', 'totalvalueINR']
        widgets = {
            'dateOfStuffing': forms.DateInput(attrs={'type':'date'}),
            'shippingBillDate': forms.DateInput(attrs={'type':'date'}),
            'size_20': forms.CheckboxInput(),
            'size_40': forms.CheckboxInput(),
        }
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['dateOfStuffing'].input_formats = ["%Y-%m-%d"]
    #     self.fields['dateOfStuffing'].label = 'Date Of Stuffing'
    #     self.fields['shippingBillDate'].input_formats = ["%Y-%m-%d"]
    #     self.fields['shippingBillDate'].label = 'Shipping Bill Date'


class TotalStuffing(ModelForm):
    class Meta:
        model = TotalStuffingValue
        exclude = ['bookingNum', 'totalPkg', 'totalGrossWt', 'totalvalueINR']
    
    # def clean(self):
    #     cleaned_data = super().clean()

    #     fields_to_uppercase = [
    #     'bookingNum', 'totalPkg', 'totalGrossWt', 'totalvalueINR'
    #     ]

    #     for field in fields_to_uppercase:
    #         if field is not None:
    #             cleaned_data[field] = cleaned_data.get(field, '').upper()
