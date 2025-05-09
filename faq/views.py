from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Aqui você encontrará respostas para as dúvidas mais comuns sobre a UNIVESP - sobre o SEI e o AVA")