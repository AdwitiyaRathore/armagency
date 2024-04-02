from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from dal import autocomplete
from django.http import JsonResponse
from django.views import View

from jobData.forms import NewData
from jobData.models import DataOfJob

from jobVGM.models import VgmModel 
from jobVGM.forms import BillingForm

from jobBOL.forms import BolForm
from jobBOL.models import BolModel

from jobACD.forms import AcdForm
from jobACD.models import AcdModel

from stuffingSheet.forms import StuffingSheetForm
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

        acd_instance = AcdModel.objects.create(
            consignee = self.object.consignee,
            placeOfReceiptOfGood = self.object.placeOfReceiptOfGood,
            portOfLoading = self.object.portOfLoading,
            grossWt = self.object.grossWt,
            noOfPkgs = self.object.noOfPkgs,
            shippingBillNo = self.object.shippingBillNo,
            marks = self.object.marks,
        )

        stuffingSheet_instance = StuffingSheetModel.objects.create(
            invoiceNo = self.object.invoiceNo,
            shippingLine = self.object.shippingLine, 
            portOfLoading = self.object.portOfLoading,
            portOfDestination = self.object.portOfDestination,
            shippingLineSeal = self.object.shippingLineSeal,
            noOfPkgs = self.object.noOfPkgs,
            grossWt = self.object.grossWt,
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
    
    def form_valid(self, form):

        response = super().form_valid(form)
        obj = form.instance

        return response


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


    