from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


def home(request):
    return render(request, 'main/home.html')


class HomePageView(TemplateView):

    template_name = "main/home.html"


def guide(request):
    return render(request, 'main/guide.html')
