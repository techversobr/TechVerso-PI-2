from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm

def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})


def index(request):
    return render(request, 'index.html')