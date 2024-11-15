from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import HttpResponse, get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from jobACD.models import AcdModel
from jobBOL.forms import BolForm
from jobBOL.models import BolModel
from jobOther.models import OtherModel
from stuffingSheet.models import StuffingSheetModel

# Create your views here.

## Class Based Views....

class BOLformDetails(LoginRequiredMixin, generic.DetailView):
    model = BolModel
    login_url = '/login/'
    redirect_field_name = 'jobBOL/bolmodel_detail.html'
    context_object_name = 'bolFormDetail'

class BOLformList(LoginRequiredMixin, generic.ListView):
    model = BolModel
    context_object_name = 'bolList'
    template_name = 'jobBOL/bolmodel_list.html'

class BOLformUpdate(LoginRequiredMixin, generic.UpdateView):
    model = BolModel
    form_class = BolForm
    login_url = '/login/'
    redirect_field_name = 'jobBOL/bolmodel_detail.html'
    

    def form_valid(self, form):
        response = super().form_valid(form)
        data_of_job_instance = self.object.index

        AcdModel.objects.update_or_create(
            index=data_of_job_instance,
            default = {
                'jobNumber': self.object.jobNumber,
                'exporterName': self.object.exporterName,
                'consignee': self.object.consignee,
                'bookingNum': self.object.bookingNum,
                'placeOfReceiptOfGood': self.object.placeOfReceiptOfGood,
                'vesselName': self.object.vesselName,
                'portOfLoading': self.object.portOfLoading,
                'portOfDischarge': self.object.portOfDischarge,
                'exporterAddress': self.object.exporterAddress,
                'grossWt' : self.object.grossWt,
                'noOfPkgs' : self.object.noOfPkgs,
                'shippingBillNo' : self.object.shippingBillNo,
                'marks' : self.object.marks,
                'noOfPkgs': self.object.noOfPkgs,
                'shippingBillNo': self.object.shippingBillNo,
                'containerNum': self.object.containerNum,
            }
        )

        StuffingSheetModel.objects.update_or_create(
            index=data_of_job_instance,
            defaults={
                'jobNumber': self.object.jobNumber,
                'bookingNum': self.object.bookingNum,
                'exporterName': self.object.exporterName,
                'invoiceNo' : self.object.invoiceNo,
                'shippingLine' : self.object.shippingLine,
                'portOfLoading' : self.object.portOfLoading,
                'portOfDestination' : self.object.portOfDestination,
                'shippingLineSeal' : self.object.shippingLineSeal,
                'noOfPkgs' : self.object.noOfPkgs,
                'grossWt' : self.object.grossWt,
                'shippingBillNo': self.object.shippingBillNo,
                'containerNum': self.object.containerNum,
                'customSeal': self.object.customSeal,
            }
        )
        OtherModel.objects.update_or_create(
            index=data_of_job_instance,
            defaults={
                'jobNumber': self.object.jobNumber,
                'bookingNum': self.object.bookingNum,
                'containerNum': self.object.containerNum,
            }
        )

        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch unique exporter info from the database and add them to the context
        context['exporterName'] = BolModel.objects.values_list('exporterName', flat=True).distinct()
        context['unique_exporterAddress'] = BolModel.objects.values_list('exporterAddress', flat=True).distinct()
        context['unique_bookingNum'] = BolModel.objects.values_list('bookingNum', flat=True).distinct()
        context['unique_descriptionOfGood'] = BolModel.objects.values_list('descriptionOfGood', flat=True).distinct()
        context['unique_customSeal'] = BolModel.objects.values_list('customSeal', flat=True).distinct()

        return context


def bol_template(request):
    query = request.GET.get('bookingNum', '')
    
    search_fields = [
    'bookingNum',
]

    # Create an empty Q object to accumulate conditions
    query_conditions = Q()

    # Loop through each field and add an OR condition
    for field in search_fields:
        query_conditions |= Q(**{f'{field}__icontains': query})

    # Use the accumulated Q object in the filter
    results = BolModel.objects.filter(query_conditions)

    return render(request, 'jobBOL/bol_template.html', {'results': results})



def search_view(request):
    query = request.GET.get('search', '') 
    
    search_fields = [
    'exporterName',
    'consignee',
    'bookingNum',
    'shippingLine',
    'containerNum',
    'portOfLoading',
]

    # Create an empty Q object to accumulate conditions
    query_conditions = Q()

    # Loop through each field and add an OR condition
    for field in search_fields:
        query_conditions |= Q(**{f'{field}__icontains': query})

    # Use the accumulated Q object in the filter
    results = BolModel.objects.filter(query_conditions)

    return render(request, 'jobBOL/search.html', {'results': results})


    