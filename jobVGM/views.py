from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import HttpResponse, render
from django.urls import reverse_lazy
from django.views import generic
from jobACD.models import AcdModel
from jobBOL.models import BolModel
from jobOther.models import OtherModel
from jobVGM.forms import BillingForm
from jobVGM.models import VgmModel
from stuffingSheet.models import StuffingSheetModel

# Create your views here.

## Class Based Views....

class VGMformDetails(LoginRequiredMixin, generic.DetailView):
    model = VgmModel
    login_url = '/login/'
    redirect_field_name = 'jobVGM/vgmmodel_detail.html'
    context_object_name = 'vgmFormDetail'
    

class VGMformList(LoginRequiredMixin, generic.ListView):
    model = VgmModel
    context_object_name = 'vgmList'
    template_name = 'jobVGM/vgmmodel_list.html'

class VGMformUpdate(LoginRequiredMixin, generic.UpdateView):
    model = VgmModel
    form_class = BillingForm
    login_url = '/login/'
    redirect_field_name = 'jobVGM/vgmmodel_detail.html'

    def form_valid(self, form):
        response = super().form_valid(form)  # Save the VgmModel instance

        # Get the related DataOfJob instance using the foreign key 'index'
        data_of_job_instance = self.object.index  # Assuming 'data_of_job' is the foreign key field in VgmModel

        # Update related models using 'index' from DataOfJob
        BolModel.objects.update_or_create(
            index=data_of_job_instance,  # Assuming BolModel has a foreign key to DataOfJob
            defaults={
                'jobNumber' : self.object.jobNumber,
                'exporterName': self.object.exporterName,
                'exporterAddress': self.object.exporterAddress,
                'IECno': self.object.IEC_no,
                'bookingNum': self.object.bookingNum,
                'containerNum': self.object.containerNum,
                'vesselName': self.object.vesselName,
            }
        )

        AcdModel.objects.update_or_create(
            index=data_of_job_instance,
            defaults={
                'jobNumber' : self.object.jobNumber,
                'exporterName': self.object.exporterName,
                'exporterAddress': self.object.exporterAddress,
                'containerNum' : self.object.containerNum,
                'vesselName' : self.object.vesselName,
                'NameOfAuthorised' : self.object.NameOfAuthorised,
                'signatureImg' : self.object.signatureImg,
            }
        )

        StuffingSheetModel.objects.update_or_create(
            index=data_of_job_instance,
            defaults={
                'jobNumber' : self.object.jobNumber,
                'exporterName': self.object.exporterName,
                'bookingNum' : self.object.containerNum,
                'containerNum' : self.object.containerNum,
                'size_20': self.object.size_20,
                'size_40': self.object.size_40,
            }
        )

        OtherModel.objects.update_or_create(
            index=data_of_job_instance,
            defaults={
                'jobNumber' : self.object.jobNumber,
                'containerNum' : self.object.containerNum,
                'bookingNum' : self.object.containerNum,
            }
        )

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch unique Exporter info from the database and add them to the context
        context['unique_exporterName'] = VgmModel.objects.values_list('exporterName', flat=True).distinct()
        context['unique_exporterAddress'] = VgmModel.objects.values_list('exporterAddress', flat=True).distinct()
        context['unique_NameOfAuthorised'] = VgmModel.objects.values_list('NameOfAuthorised', flat=True).distinct()
        context['unique_DesignationOfAuthorised'] = VgmModel.objects.values_list('DesignationOfAuthorised', flat=True).distinct()
        context['unique_contactDetail'] = VgmModel.objects.values_list('contactDetail', flat=True).distinct()
        context['unique_bookingNum'] = VgmModel.objects.values_list('bookingNum', flat=True).distinct()

        return context
    
#__________________________________________________________________________________
## Different VGM forms using Class Based Views....
# For Hapag, Cosco, ....HMM.
class VgmForm1Detail(LoginRequiredMixin, generic.DetailView):
    model = VgmModel
    login_url = '/login/'
    template_name = 'jobVGM/vgm_type1.html'
    context_object_name = 'vgmForm1'

    def get_queryset(self):
        return VgmModel.objects.filter(pk=self.kwargs['pk'])

# For MSC.
class VgmForm2Detail(LoginRequiredMixin, generic.DetailView):
    model = VgmModel
    login_url = '/login/'
    template_name = 'jobVGM/vgm_type2.html'
    context_object_name = 'vgmForm2'

    def get_queryset(self):
        return VgmModel.objects.filter(pk=self.kwargs['pk'])

# For CMA, ANL.
class VgmForm3Detail(LoginRequiredMixin, generic.DetailView):
    model = VgmModel
    login_url = '/login/'
    template_name = 'jobVGM/vgm_type3.html'
    context_object_name = 'vgmForm3'

    def get_queryset(self):
        return VgmModel.objects.filter(pk=self.kwargs['pk'])

# For Evergreen Line.
class VgmForm4Detail(LoginRequiredMixin, generic.DetailView):
    model = VgmModel
    login_url = '/login/'
    template_name = 'jobVGM/vgm_type4.html'
    context_object_name = 'vgmForm4'

    def get_queryset(self):
        return VgmModel.objects.filter(pk=self.kwargs['pk'])

#_________________________________________________________________________________

## Function based views....

def search_view(request):
    query = request.GET.get('search', '') 
    
    search_fields = [
    'exporterName',
    'IEC_no',
    'NameOfAuthorised',
    'DesignationOfAuthorised',
    'containerNum',
    'bookingNum'
]

    # Create an empty Q object to accumulate conditions
    query_conditions = Q()

    # Loop through each field and add an OR condition
    for field in search_fields:
        query_conditions |= Q(**{f'{field}__icontains': query})

    # Use the accumulated Q object in the filter
    results = VgmModel.objects.filter(query_conditions)

    return render(request, 'jobVGM/search.html', {'results': results})