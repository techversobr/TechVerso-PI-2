from django.shortcuts import render, redirect
from django.urls import reverse  # Importação corrigida
from django.http import HttpResponse
from .models import JobPost
from .forms import JobPostForm

def index(request):
    create_url = reverse('create')  # Gera a URL para 'create'
    list_url = reverse('list')  # Gera a URL para 'list'
    return HttpResponse(f"""
        <p>Aqui falaremos sobre as vagas.</p>
        <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="{create_url}">Postar Vagas</a></li>
            <li><a class="dropdown-item" href="{list_url}">Listar Vagas</a></li>
        </ul>
        <button onclick="window.history.back()">Voltar</button>
    """)

def form_django(request):
    form = JobPostForm()
    context = {
        'form': form,
    }
    return render(request, '/templates/create_job_post.html', context=context)

def create_job_post(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no banco de dados
            return redirect('list')  # Redireciona para a página de listagem
    else:
        form = JobPostForm()
    return render(request, 'create_job_post.html', {'form': form})

def list_job_posts(request):
    jobs = JobPost.objects.all()  # Obtém todas as vagas do banco de dados
    return render(request, 'list_job_posts.html', {'jobs': jobs})  # Passa o contexto 'jobs'