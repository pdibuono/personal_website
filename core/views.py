from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class ContactCreateView(CreateView):
    model = Contact
    template_name = "contact/contact_form.html"
    fields = ['title', 'First_Name', 'Last_Name', 'email', 'description']
    success_url = reverse_lazy('success')

class Success(TemplateView):
    template_name = "success.html"

class AboutMeView(TemplateView):
    template_name = 'aboutme.html'

class ContactInfoView(TemplateView):
    template_name = 'contact_info.html'

