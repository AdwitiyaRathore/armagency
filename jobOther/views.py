from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import HttpResponse, get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from jobOther.forms import OtherForm
from jobOther.models import OtherModel
from stuffingSheet.models import StuffingSheetModel

# Create your views here.

## Class Based Views....

class JobOtherDetails(LoginRequiredMixin, generic.DetailView):
    model = OtherModel
    login_url = '/login/'
    redirect_field_name = 'jobOther/otherModel_detail.html'
    context_object_name = 'otherDetail'

class JobOtherList(LoginRequiredMixin, generic.ListView):
    model = StuffingSheetModel
    context_object_name = 'otherList'
    template_name = 'jobOther/otherModel_list.html'

class JobOtherUpdate(LoginRequiredMixin, generic.UpdateView):
    model = OtherModel
    form_class = OtherForm
    login_url = '/login/'
    redirect_field_name = 'jobOther/otherModel_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch unique exporter info from the database and add them to the context
        context['unique_PanNo'] = OtherModel.objects.values_list('PanNo', flat=True).distinct()
        context['unique_ChaName'] = OtherModel.objects.values_list('ChaName', flat=True).distinct()
        context['unique_bookingNum'] = OtherModel.objects.values_list('bookingNum', flat=True).distinct()

        return context


## Function Based Views........................

def search_view(request):
    query = request.GET.get('search', '')
    
    search_fields = [
    'containerNum',
    'bookingNum',
]

    # Create an empty Q object to accumulate conditions
    query_conditions = Q()

    # Loop through each field and add an OR condition
    for field in search_fields:
        query_conditions |= Q(**{f'{field}__icontains': query})

    # Use the accumulated Q object in the filter
    results = OtherModel.objects.filter(query_conditions)

    return render(request, 'jobOther/search.html', {'results': results})