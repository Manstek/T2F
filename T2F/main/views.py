from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'main/about.html'


class TechView(TemplateView):
    template_name = 'main/tech.html'
