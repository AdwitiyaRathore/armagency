from datetime import date, datetime
from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Sum
from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from jobACD.forms import AcdForm
from jobACD.models import AcdModel
from jobBOL.forms import BolForm
from jobBOL.models import BolModel
from jobData.forms import NewData
from jobData.models import DataOfJob
from jobOther.forms import OtherForm
from jobOther.models import OtherModel
from jobVGM.forms import BillingForm
from jobVGM.models import VgmModel
from stuffingSheet.forms import StuffingSheetForm
from stuffingSheet.models import StuffingSheetModel

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
        # Get the number of bookings from the form
        num_bookings = form.cleaned_data.get('noOfBooking')

        # Retrieve the data for each booking
        original_job_data = {
            'jobNumber': form.cleaned_data.get('jobNumber'),
            'noOfBooking': 1,  # Set to 1 because this will be individual booking now
            'container_no': form.cleaned_data.get('container_no'),
            'shippingLine': form.cleaned_data.get('shippingLine'),
            'Forwarder': form.cleaned_data.get('Forwarder'),
            'bookingNum': form.cleaned_data.get('bookingNum'),
            'exporterName': form.cleaned_data.get('exporterName'),
            'exporterAddress': form.cleaned_data.get('exporterAddress'),
            'size_20': form.cleaned_data.get('size_20'),
            'size_40': form.cleaned_data.get('size_40'),
            'todayDate': form.cleaned_data.get('todayDate', timezone.now().date()),
        }

        for _ in range(num_bookings):
            # Create a new instance with the same data but a new primary key
            self.object = DataOfJob(**original_job_data)
            self.object.pk = None  # This creates a new instance with a new primary key
            self.object.save()  # Save the new instance

            # Define size_20 and size_40 based on the tues_1 and tues_2 values
            size_20 = self.object.size_20
            size_40 = self.object.size_40

            # Create instances for related models
            VgmModel.objects.create(
                jobNumber = self.object.jobNumber,
                containerNum = self.object.container_no,
                exporterName=self.object.exporterName,
                exporterAddress=self.object.exporterAddress,
                size_20=size_20,
                size_40=size_40,
                bookingNum=self.object.bookingNum,
            )

            BolModel.objects.create(
                jobNumber = self.object.jobNumber,
                containerNum = self.object.container_no,
                shippingLine=self.object.shippingLine,
                bookingNum=self.object.bookingNum,
                exporterName=self.object.exporterName,
                exporterAddress=self.object.exporterAddress,
            )

            AcdModel.objects.create(
                jobNumber = self.object.jobNumber,
                containerNum = self.object.container_no,
                bookingNum=self.object.bookingNum,
                exporterName=self.object.exporterName,
                exporterAddress=self.object.exporterAddress,
            )

            StuffingSheetModel.objects.create(
                jobNumber = self.object.jobNumber,
                containerNum = self.object.container_no,
                bookingNum=self.object.bookingNum,
                exporterName=self.object.exporterName,
                shippingLine=self.object.shippingLine,
                size_20=size_20,
                size_40=size_40,
            )

            OtherModel.objects.create(
                jobNumber = self.object.jobNumber,
                containerNum = self.object.container_no,
                bookingNum=self.object.bookingNum,
            )

        return super().form_valid(form)
    
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

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     size_20 = self.object.size_20
    #     size_40 = self.object.size_40

    #     # Create instances for related models
    #     VgmModel.objects.create(
    #         jobNumber = self.object.jobNumber,
    #         exporterName=self.object.exporterName,
    #         exporterAddress=self.object.exporterAddress,
    #         size_20=size_20,
    #         size_40=size_40,
    #         bookingNum=self.object.bookingNum,
    #     )

    #     BolModel.objects.create(
    #         jobNumber = self.object.jobNumber,
    #         shippingLine=self.object.shippingLine,
    #         bookingNum=self.object.bookingNum,
    #         exporterName=self.object.exporterName,
    #         exporterAddress=self.object.exporterAddress,
    #     )

    #     AcdModel.objects.create(
    #         jobNumber = self.object.jobNumber,
    #         bookingNum=self.object.bookingNum,
    #         exporterName=self.object.exporterName,
    #         exporterAddress=self.object.exporterAddress,
    #     )

    #     StuffingSheetModel.objects.create(
    #         jobNumber = self.object.jobNumber,
    #         bookingNum=self.object.bookingNum,
    #         exporterName=self.object.exporterName,
    #         shippingLine=self.object.shippingLine,
    #         size_20=size_20,
    #         size_40=size_40,
    #     )

    #     OtherModel.objects.create(
    #         jobNumber = self.object.jobNumber,
    #         bookingNum=self.object.bookingNum,
    #     )

    #     return response

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