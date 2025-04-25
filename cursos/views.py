from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Aqui vocÊ encontrara indicações de cursos relacionados ao seu eixo.")