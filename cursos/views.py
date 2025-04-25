from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<p>Aqui vocÊ encontrara indicações de cursos relacionados ao seu eixo.</p>'
                        '<button onclick="window.history.back()">Voltar</button>')