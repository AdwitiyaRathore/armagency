from django.shortcuts import render, HttpResponse
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

from jobOther.forms import OtherForm
from jobOther.models import OtherModel

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
        response = super().form_valid(form)

        
        bol_instance = BolModel.objects.create(
            containerNum = self.object.containerNum,
            vesselName = self.object.vesselName,
        )

        acd_instance = AcdModel.objects.create(
            containerNum = self.object.containerNum,
            vesselName = self.object.vesselName,
            NameOfAuthorised = self.object.NameOfAuthorised,
            signatureImg = self.object.signatureImg,
        )

        stuffingSheet_instance = StuffingSheetModel.objects.create(
            bookingNum = self.object.containerNum,
        )

        otherJob_instance = OtherModel.objects.create(
            containerNum = self.object.containerNum,
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

    def form_valid(self, form):

        response = super().form_valid(form)
        obj = form.instance

        return response
    
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