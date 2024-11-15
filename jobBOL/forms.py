from django import forms
from django.forms import ModelForm

from .models import BolModel


class BolForm(ModelForm):
    jobNumber = forms.IntegerField(label='Job Number')
    exporterName = forms.CharField(label='Exporter Name', max_length=255)
    exporterAddress = forms.Textarea()
    consignee = forms.CharField(required=False, label='Consignee', max_length=255)
    notifyDelivery = forms.CharField(required=False, label='Notify Delivery', max_length=255)
    bookingNo = forms.CharField(required=False, label='Booking No', max_length=255)
    shippingLine = forms.CharField(required=False, label='Shipping Line', max_length=255)
    armAddress = forms.CharField(required=False, label='Arm Address', max_length=255)
    initialCarriage_mode = forms.CharField(required=False, label='Initial Carriage Mode', max_length=255)
    placeOfReceiptOfGood = forms.CharField(required=False, label='Place Of Receipt Of Good', max_length=255)
    vesselName = forms.CharField(required=False, label='Vessel Name', max_length=255)
    portOfLoading = forms.CharField(required=False, label='Port Of Loading', max_length=255)
    portOfDestination = forms.CharField(required=False, label='Port Of Destination', max_length=255)
    finalDestination = forms.CharField(required=False, label='Final Destination', max_length=255)
    marks = forms.CharField(required=False, label='Marks', max_length=255)
    noOfPkgs = forms.IntegerField(required=False, label='No Of Pkgs')
    grossWt = forms.FloatField(required=False, label='Gross Wt')
    netWt = forms.FloatField(required=False, label='Net Wt')
    CBM = forms.FloatField(required=False, label='CBM')
    descriptionOfGood = forms.CharField(required=False, label='Description Of Good', max_length=255)
    shippingBillNo = forms.IntegerField(required=False, label='Shipping Bill No', )
    invoiceNo = forms.CharField(required=False, label='Invoice No', max_length=255)
    hsCode = forms.CharField(required=False, label='Hs Code', max_length=255)
    poCode = forms.CharField(required=False, label='Po Code', max_length=255)
    containerNo = forms.CharField(required=False, label='Container No', max_length=255)
    shippingLineSeal = forms.CharField(required=False, label='Shipping Line Seal', max_length=255)
    customSeat = forms.IntegerField(required=False, label='Custom Seat')
    freight = forms.CharField(required=False, label='Freight', max_length=255)
    dateOfIssue = forms.DateField(required=False, label='DateOfIssue')

    widgets = {
            'exporterAddress': forms.Textarea(attrs={'rows': 5}),
        }
    
    class Meta:
        model = BolModel
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        fields_to_uppercase = [
        'jobNumber', 'exporterName', 'exporterAddress', 'gstin', 'consignee',
        'notifyDelivery', 'bookingNum', 'shippingLine', 'armAddress',
        'initialCarriage_mode', 'placeOfReceiptOfGood', 'vesselName',
        'portOfLoading', 'portOfDestination', 'finalDestination', 'marks',
        'descriptionOfGood', 'invoiceNo', 'hsCode', 'poCode', 'containerNum',
        'shippingLineSeal', 'customSeal', 'freight'
        ]

        for field in fields_to_uppercase:
            value = cleaned_data.get(field)
            if value:
                cleaned_data[field] = str(value).upper()

        return cleaned_data