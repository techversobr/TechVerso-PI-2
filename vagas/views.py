from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse
from .models import JobPost
from .forms import JobPostForm

def index(request):
    return HttpResponse("""
        <p>Aqui falaremos sobre as vagas.</p>
        <button onclick="window.history.back()">Voltar</button>
    """)

def create_job_post(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_job_posts')  # redirecione para a página de listagem
    else:
        form = JobPostForm()
    return render(request, 'create_job_post.html', {'form': form})

def list_job_posts(request):
    job_posts = JobPost.objects.all()
    return render(request, 'list_job_posts.html', {'job_posts': job_posts})