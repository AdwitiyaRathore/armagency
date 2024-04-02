from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (DetailView, CreateView, ListView, UpdateView, DeleteView, TemplateView)
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from datetime import datetime
from django.db.models import Sum


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

from jobOther.forms import OtherForm
from jobOther.models import OtherModel
# Create your views here.

## Class Based Views....

class jobListView(ListView):
    model = DataOfJob
    context_object_name = 'showJobList'

class CreateJobView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'jobData/dataofjob_detail.html'
    model = DataOfJob
    form_class = NewData

    def form_valid(self, form):
        response = super().form_valid(form)

        if self.object.tues_1 == 1 and self.object.tues_2 == 2:
            size_20 = True
            size_40 = True 
        elif self.object.tues_1 == 1:
            size_20 = True
            size_40 = False
        elif self.object.tues_2 == 2:
            size_20 = False
            size_40 = True
        else:
            size_20 = True
            size_40 = True

        

        vgm_instance = VgmModel.objects.create(
            exporterName = self.object.exporterName,
            exporterAddress = self.object.exporterAddress,
            size_20 = size_20,
            size_40 = size_40,
            bookingNum = self.object.bookingNum,
        )
        
        bol_instance = BolModel.objects.create(
            shippingLine = self.object.shippingLine,
            bookingNum = self.object.bookingNum,
            exporterName = self.object.exporterName, 
            exporterAddress = self.object.exporterAddress,
        )

        acd_instance = AcdModel.objects.create(
            bookingNum = self.object.bookingNum,
            exporterName = self.object.exporterName, 
            exporterAddress = self.object.exporterAddress,
        )

        stuffingSheet_instance = StuffingSheetModel.objects.create(
            bookingNum = self.object.bookingNum,
            exporterName = self.object.exporterName, 
            shippingLine = self.object.shippingLine,
            size_20 = size_20,
            size_40 = size_40,
        )

        otherJob_instance = OtherModel.objects.create(
            bookingNum = self.object.bookingNum,
        )
        
        return super().form_valid(form)
        # return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch unique Exporter info from the database and add them to the context
        context['unique_exporterName'] = DataOfJob.objects.values_list('exporterName', flat=True).distinct()
        context['unique_exporterAddress'] = DataOfJob.objects.values_list('exporterAddress', flat=True).distinct()
        context['unique_Forwarder'] = DataOfJob.objects.values_list('Forwarder', flat=True).distinct()
        context['unique_bookingNum'] = DataOfJob.objects.values_list('bookingNum', flat=True).distinct()

        return context


class JobDetailView(DetailView):
    model = DataOfJob
    context_object_name = 'showJobDetail'
    template_name = 'jobData/dataofjob_detail.html'


class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = DataOfJob
    form_class = NewData
    login_url = '/login/'
    redirect_field_name = 'jobData/dataofjob_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch unique Exporter info from the database and add them to the context
        context['unique_exporterName'] = DataOfJob.objects.values_list('exporterName', flat=True).distinct()
        context['unique_exporterAddress'] = DataOfJob.objects.values_list('exporterAddress', flat=True).distinct()
        context['unique_Forwarder'] = DataOfJob.objects.values_list('Forwarder', flat=True).distinct()
        context['unique_bookingNum'] = DataOfJob.objects.values_list('bookingNum', flat=True).distinct()

        return context
    

class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = DataOfJob
    success_url = reverse_lazy('jobData:jobList')



## Function Based Views....................................................


def totalTues(from_date, to_date):
    # Convert date strings to datetime objects
    from_date_obj = datetime.strptime(from_date, "%Y-%m-%d")
    to_date_obj = datetime.strptime(to_date, "%Y-%m-%d")

    # Calculate the sum of tues_1 and tues_2 between the given date range
    total_tues = DataOfJob.objects.filter(todayDate__range=[from_date_obj, to_date_obj]).aggregate(
        total_tues_1=Sum('tues_1'),
        total_tues_2=Sum('tues_2')
    )

    # Access the sums from the result
    sum_tues_1 = total_tues['total_tues_1'] or 0
    sum_tues_2 = total_tues['total_tues_2'] or 0

    return sum_tues_1, sum_tues_2



def jobFilterListView(request):
    from_date_str = request.POST.get('from_date', '')
    to_date_str = request.POST.get('to_date', '')

    if from_date_str != '' and to_date_str != '':

        totalTues1, totalTues2 = totalTues(from_date_str, to_date_str)
        total_tues = totalTues1 + totalTues2
        
        context = {
            'from_date_str':from_date_str,
            'to_date_str':to_date_str,
            'total_tues':total_tues
        }
    else:
        context = {
            'from_date_str':'',
            'to_date_str':'',
            'total_tues':'',
        }
    # totalTues1, totalTues2 = totalTues(query_conditions)

    return render(request, 'jobData/jobFilterList.html', context)



def search_view(request):
    query = request.GET.get('search', '') 
    
    search_fields = [
    'jobNumber',
    'shippingLine',
    'Forwarder',
    'bookingNum',
    'size_20',
    'size_40',
    'tues_1',
    'tues_2',
    'exporterName',
    'exporterAddress',
    ]

    # Create an empty Q object to accumulate conditions
    query_conditions = Q()

    # Loop through each field and add an OR condition
    for field in search_fields:
        query_conditions |= Q(**{f'{field}__icontains': query})

    # Use the accumulated Q object in the filter
    results = DataOfJob.objects.filter(query_conditions)

    return render(request, 'jobData/search.html', {'results': results})