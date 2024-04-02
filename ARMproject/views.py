from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'index.html'

class Entry(TemplateView):
    template_name = 'entry.html'

class Exit(TemplateView):
    template_name = 'exit.html'