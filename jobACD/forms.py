from django import forms
from django.forms import ModelForm
from .models import AcdModel

class AcdForm(ModelForm):
    jobNumber = forms.IntegerField(required=False, label='Job Number')
    bookingNum = forms.CharField(required=False, label='Booking Num')
    exporterAddress = forms.Textarea()
    consignee = forms.CharField(required=False, label='Consignee')
    nameOfOceanCarrier = forms.CharField(required=False, label='Name Of Ocean Carrier')
    vesselName = forms.CharField(required=False, label='Vessel Name')
    placeOfReceiptOfGood = forms.CharField(required=False, label='Place Of Receipt Of Good')
    portOfLoading = forms.CharField(required=False, label='Port Of Loading')
    portOfDischarge = forms.CharField(required=False, label='Port Of Discharge')
    placeOfDeliveryWithStateCode = forms.CharField(required=False, label='Place Of Delivery With State Code')
    containerNum = forms.CharField(required=False, label='Container Num')
    customSeal = forms.CharField(required=False, label='Custom Seal')
    shippingBillNo = forms.CharField(required=False, label='Shipping Bill No')
    marks = forms.CharField(required=False, label='Marks')
    noOfPkgs = forms.IntegerField(required=False, label='No Of Pkgs')
    fullCommondityDescription = forms.CharField(required=False, label='Full Commondity Description')
    grossWt = forms.CharField(required=False, label='Gross Wt')
    htsCode = forms.CharField(required=False, label='HTC Code')
    placeOfIssueOfCargo = forms.CharField(required=False, label='place Of Issue Of Cargo')
    exporterName = forms.CharField(required=False, label='Exporter Name')
    NameOfAuthorised = forms.CharField(required=False, label='Name Of Authorised')
    signatureImg = forms.ImageField(required=False, label='Signature Img')

    class Meta:
        model = AcdModel
        fields = '__all__'
        widgets = {
            'dateOfIssueOfCargo': forms.DateInput(attrs={'type':'date'})
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['dateOfIssueOfCargo'].input_formats = ["%Y-%m-%d"]
    #     self.fields['dateOfIssueOfCargo'].label = 'dateOfIssueOfCargo'

    # def clean(self):
    #     cleaned_data = super().clean()

    #     fields_to_uppercase = [
    #     'jobNumber', 'bookingNum', 'exporterAddress', 'consignee',
    #     'nameOfOceanCarrier', 'vesselName', 'placeOfReceiptOfGood',
    #     'portOfLoading', 'portOfDischarge', 'placeOfDeliveryWithStateCode',
    #     'containerNum', 'customSeal', 'shippingBillNo', 'marks', 'noOfPkgs',
    #     'fullCommondityDescription', 'grossWt', 'htsCode', 'placeOfIssueOfCargo',
    #     'dateOfIssueOfCargo', 'exporterName', 'NameOfAuthorised', 'signatureImg'
    #     ]

    #     for field in fields_to_uppercase:
    #         if field is not None:
    #             cleaned_data[field] = cleaned_data.get(field, '').upper()