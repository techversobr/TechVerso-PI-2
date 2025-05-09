from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Aqui você saberá como nos acompanhar nas principais redes sociais e como nos contatar.")