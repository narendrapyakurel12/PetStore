from django.shortcuts import render
from.models import *
from .forms import *

from django.views.generic import *


class HomeView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ServicesView(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicelist'] = Services.objects.all()
        context['teamlist'] = Team.objects.all()
        return context


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class=ContactForm
    success_url='/'


class NewsView(TemplateView):
    template_name = 'news.html'
