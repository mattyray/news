from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
class JsGptQuizView(TemplateView):
    template_name = 'jsgptquiz.html'

# Create your views here.
