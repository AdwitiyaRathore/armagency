from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from dal import autocomplete
from django.http import JsonResponse
from django.views import View
from django.db.models import Sum


## App imports...

from jobData.forms import NewData
from jobData.models import DataOfJob

from jobVGM.models import VgmModel 
from jobVGM.forms import BillingForm

from jobBOL.forms import BolForm
from jobBOL.models import BolModel

from jobACD.forms import AcdForm
from jobACD.models import AcdModel

from stuffingSheet.forms import StuffingSheetForm
from stuffingSheet.models import StuffingSheetModel, TotalStuffingValue
# Create your views here.

## Class Based Views....

class StuffingSheetformDetails(LoginRequiredMixin, generic.DetailView):
    model = StuffingSheetModel
    login_url = '/login/'
    redirect_field_name = 'stuffingSheet/stuffingSheetModel_detail.html'
    context_object_name = 'stuffingSheetDetail'

class StuffingSheetformList(LoginRequiredMixin, generic.ListView):
    model = StuffingSheetModel
    context_object_name = 'stuffingSheetList'
    template_name = 'stuffingSheet/stuffingSheetModel_list.html'

class StuffingSheetformUpdate(LoginRequiredMixin, generic.UpdateView):
    model = StuffingSheetModel
    form_class = StuffingSheetForm
    login_url = '/login/'
    redirect_field_name = 'stuffingSheet/stuffingSheetModel_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch unique Exporter info from the database and add them to the context
        context['unique_exporterName'] = StuffingSheetModel.objects.values_list('exporterName', flat=True).distinct()
        context['unique_invoiceNo'] = StuffingSheetModel.objects.values_list('invoiceNo', flat=True).distinct()
        context['unique_shippingLineSeal'] = StuffingSheetModel.objects.values_list('shippingLineSeal', flat=True).distinct()
        context['unique_customSeal'] = StuffingSheetModel.objects.values_list('customSeal', flat=True).distinct()
        context['unique_bookingNum'] = StuffingSheetModel.objects.values_list('bookingNum', flat=True).distinct()

        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        obj = form.instance

        return response

def calculateAndStoreTotal(booking_number):
    stuffing_sheet_results = StuffingSheetModel.objects.filter(bookingNum=booking_number)

    total_pkg_sum = stuffing_sheet_results.aggregate(Sum('noOfPkgs'))['noOfPkgs__sum'] or 0
    total_gross_wt_sum = stuffing_sheet_results.aggregate(Sum('grossWt'))['grossWt__sum'] or 0
    total_value_inr_sum = stuffing_sheet_results.aggregate(Sum('valueINR'))['valueINR__sum'] or 0

    total_stuffing, created = TotalStuffingValue.objects.get_or_create(
        bookingNum=booking_number,
        defaults={
            'totalPkg': total_pkg_sum,
            'totalGrossWt': total_gross_wt_sum,
            'totalvalueINR': total_value_inr_sum,
        }
    )
    if not created:
        total_stuffing.totalPkg = total_pkg_sum
        total_stuffing.totalGrossWt = total_gross_wt_sum
        total_stuffing.totalvalueINR = total_value_inr_sum
        total_stuffing.save()

    return total_pkg_sum, total_gross_wt_sum, total_value_inr_sum



def stuffingSheetTemplate(request):
    query = request.GET.get('bookingNum', '')

    search_fields = ['bookingNum']

    query_conditions = Q()

    for field in search_fields:
        query_conditions |= Q(**{f'{field}__icontains': query})

    stuffing_results = StuffingSheetModel.objects.filter(query_conditions)
    
    total_pkg_sum, total_gross_wt_sum, total_value_inr_sum = calculateAndStoreTotal(query)
    total_results = TotalStuffingValue.objects.filter(bookingNum=query)

    context = {
        'stuffingResults': stuffing_results,
        'totalResults': total_results,
        'total_pkg_sum': total_pkg_sum,
        'total_gross_wt_sum': total_gross_wt_sum,
        'total_value_inr_sum': total_value_inr_sum,
    }

    return render(request, 'StuffingSheet/stuffingSheet_template.html', context)


def search_view(request):
    query = request.GET.get('search', '') 
    
    search_fields = [
    'exporterName',
    'depot',
    'bookingNum',
    'containerNum',
    'shippingLine',
    'customSeal',
]

    # Create an empty Q object to accumulate conditions
    query_conditions = Q()

    # Loop through each field and add an OR condition
    for field in search_fields:
        query_conditions |= Q(**{f'{field}__icontains': query})

    # Use the accumulated Q object in the filter
    results = StuffingSheetModel.objects.filter(query_conditions)

    return render(request, 'stuffingSheet/search.html', {'results': results})    