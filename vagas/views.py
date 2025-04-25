from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Aqui falaremos sobre as vagas.")

# Create your views here.
