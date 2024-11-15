from dal import autocomplete
from django import forms
from django.forms import ModelForm

from .models import VgmModel


class BillingForm(ModelForm):

    ## Field Custom Name....
    jobNumber = forms.IntegerField(required=False, label='Job Number')
    exporterName = forms.CharField(required=False, label='Exporter Name')
    exporterAddress = forms.Textarea()
    IEC_no = forms.IntegerField(required=False, label='IEC No')
    NameOfAuthorised = forms.CharField(required=False, label='Name Of Authorised')
    bookingNum = forms.CharField(required=False, label='Booking No')
    DesignationOfAuthorised = forms.CharField(required=False, label='Designation Of Authorised')
    contactDetail = forms.IntegerField(required=False, label='Contact Detail')
    containerNum = forms.CharField(required=False, label='Container No')
    WeighBridgeRegistration = forms.CharField(required=False, label='WeighBridge Registration')
    WeighBridgeAddress = forms.CharField(required=False, label='WeighBridge Address')
    emptyContainerMass = forms.FloatField(required=False, label='Empty Container Mass')
    goodMass = forms.FloatField(required=False, label='Good Mass')
    dateOfWeigh = forms.DateField(required=False, label='Date of WEigh')
    timeofWeigh = forms.TimeField(required=False, label='Time of WEigh(Hr:Min)')
    cargoWeight = forms.IntegerField(required=False, label='Cargo Weight')
    containerWeight = forms.IntegerField(required=False, label='Container Weight')
    verifiedGrossMass = forms.FloatField(required=False, label='Verified Gross Mass')
    weightmentSlipNum = forms.CharField(required=False, label='Weightment Slip No')
    unitOfMeasure = forms.CharField(required=False, label='Unit Of Measure')
    typeOF = forms.CharField(required=False, label='Type Of')
    ifHazardous = forms.CharField(required=False, label='If Hazardous')
    vesselName = forms.CharField(required=False, label='Vessel Name')
    vcnNo = forms.CharField(required=False, label='Vcn No')

    
    widget=forms.TextInput(attrs={'placeholder': None})
    
    class Meta:
        model = VgmModel
        exclude = ['verifiedGrossMass', 'todayDate']
        # fields = '__all__'
        widgets = {
            'timeofWeigh' : forms.DateInput(attrs={'type':'time'}),
            'dateOfWeigh': forms.DateInput(attrs={'type':'date'}),
            'exporterAddress': forms.Textarea(attrs={'rows': 5}),
            'size_20': forms.CheckboxInput(),
            'size_40': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dateOfWeigh'].input_formats = ["%Y-%m-%d"]
        self.fields['dateOfWeigh'].label = 'Date Of Weigh'
        self.fields['timeofWeigh'].input_formats = ["%H-%m"]
        self.fields['timeofWeigh'].label = 'Time of Weigh'

    def __init__(self, *args, **kwargs):
        super(BillingForm, self).__init__(*args, **kwargs)

        # Pre-select the exporterName field with the value from the instance
        instance = getattr(self, 'instance', None)
        if instance and instance.exporterName:
            self.fields['exporterName'].queryset = VgmModel.objects.filter(exporterName=instance.exporterName)
            self.fields['exporterName'].initial = instance.exporterName
        else:
            self.fields['exporterName'].queryset = VgmModel.objects.none()
    
    def clean(self):
        cleaned_data = super().clean()

        fields_to_uppercase = [
            'exporterName', 'exporterAddress', 'NameOfAuthorised', 'bookingNum',
            'DesignationOfAuthorised', 'containerNum', 'WeighBridgeRegistration',
            'WeighBridgeAddress', 'weightmentSlipNum', 'unitOfMeasure', 'typeOF',
            'ifHazardous', 'vesselName', 'vcnNo'
        ]

        for field in fields_to_uppercase:
            value = cleaned_data.get(field)
            if field is not None:
                cleaned_data[field] = str(value).upper()