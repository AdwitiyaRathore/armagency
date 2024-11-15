from django import forms
from django.forms import ModelForm

from .models import OtherModel


class OtherForm(ModelForm):
    
    jobNumber = forms.IntegerField(required=False, label='Job Number')
    bookingNum = forms.CharField(required=False, label='Booking Num')
    containerNum = forms.CharField(required=False, label='Container No')
    containerMethodType = forms.CharField(required=False, label='Container Method Type')
    PanNo = forms.CharField(required=False, label='Pan No')
    ChaName = forms.CharField(required=False, label='CHA Name')

    class Meta:
        model = OtherModel
        fields = '__all__'
        widgets = {
                'doExpityDate': forms.DateInput(attrs={'type':'date'}),
                'dispatchDate': forms.DateInput(attrs={'type':'date'}),
                'invoiceDate': forms.DateInput(attrs={'type':'date'}),
                'vessealCutOffDate': forms.DateInput(attrs={'type':'date'}),
                'handoverDate': forms.DateInput(attrs={'type':'date'}),
                'allotmentDate': forms.DateInput(attrs={'type':'date'}),
                'seaPortInDate': forms.DateInput(attrs={'type':'date'}),
        }
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doExpityDate'].input_formats = ["%Y-%m-%d"]
        self.fields['doExpityDate'].label = 'Do Expity Date'

        self.fields['dispatchDate'].input_formats = ["%Y-%m-%d"]
        self.fields['dispatchDate'].label = 'Dispatch Date'

        self.fields['invoiceDate'].input_formats = ["%Y-%m-%d"]
        self.fields['invoiceDate'].label = 'Invoice Date'

        self.fields['vessealCutOffDate'].input_formats = ["%Y-%m-%d"]
        self.fields['vessealCutOffDate'].label = 'Vesseal Cut Off Date'

        self.fields['handoverDate'].input_formats = ["%Y-%m-%d"]
        self.fields['handoverDate'].label = 'Handover Date'

        self.fields['allotmentDate'].input_formats = ["%Y-%m-%d"]
        self.fields['allotmentDate'].label = 'Allotment Date'

        self.fields['seaPortInDate'].input_formats = ["%Y-%m-%d"]
        self.fields['seaPortInDate'].label = 'Sea Port In Date'



    def clean(self):
        cleaned_data = super().clean()

        fields_to_uppercase = [ 'jobNumber', 'bookingNum', 'containerMethodType', 'PanNo', 'ChaName']

        for field in fields_to_uppercase:
            value = cleaned_data.get(field)
            if value:
                cleaned_data[field] = str(value).upper()