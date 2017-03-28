#from django.views.generic import TemplateView


# class AboutView(TemplateView):
#     template_name = "about.html"

from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return render(request, "questions/about.html")


def get_post(request):
    return HttpResponse(request.GET.urlencode())
