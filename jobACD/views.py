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

class ACDformDetails(LoginRequiredMixin, generic.DetailView):
    model = AcdModel
    login_url = '/login/'
    redirect_field_name = 'jobACD/acdmodel_detail.html'
    context_object_name = 'acdFormDetail'

class ACDformList(LoginRequiredMixin, generic.ListView):
    model = AcdModel
    context_object_name = 'acdList'
    template_name = 'jobACD/acdmodel_list.html'

class ACDformUpdate(LoginRequiredMixin, generic.UpdateView):
    model = AcdModel
    form_class = AcdForm
    login_url = '/login/'
    redirect_field_name = 'jobACD/acdmodel_detail.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        stuffingSheet_instance = StuffingSheetModel.objects.create(
            customSeal = self.object.customSeal,
        )

        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch unique exporter info from the database and add them to the context
        context['unique_consignee'] = AcdModel.objects.values_list('consignee', flat=True).distinct()
        context['unique_exporterAddress'] = AcdModel.objects.values_list('exporterAddress', flat=True).distinct()
        context['unique_bookingNum'] = AcdModel.objects.values_list('bookingNum', flat=True).distinct()
        context['unique_shippingBillNo'] = AcdModel.objects.values_list('shippingBillNo', flat=True).distinct()
        context['unique_customSeal'] = AcdModel.objects.values_list('customSeal', flat=True).distinct()

        return context 
    
    def form_valid(self, form):

        response = super().form_valid(form)
        obj = form.instance

        return response

class AcdTemplate(LoginRequiredMixin, generic.DetailView):
    model = AcdModel
    login_url = '/login/'
    template_name = 'jobACD/acdTemplate.html'
    context_object_name = 'acdForm'

    def get_queryset(self):
        return AcdModel.objects.filter(pk=self.kwargs['pk'])

def search_view(request):
    query = request.GET.get('search', '') 
    
    search_fields = [
    'exporterName',
    'consignee',
    'bookingNum',
    'containerNum',
]

    # Create an empty Q object to accumulate conditions
    query_conditions = Q()

    # Loop through each field and add an OR condition
    for field in search_fields:
        query_conditions |= Q(**{f'{field}__icontains': query})

    # Use the accumulated Q object in the filter
    results = AcdModel.objects.filter(query_conditions)

    return render(request, 'jobACD/search.html', {'results': results})


    