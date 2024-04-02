from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'