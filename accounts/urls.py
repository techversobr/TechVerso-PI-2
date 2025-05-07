from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('formularios/form_cursos/', views.form_cursos, name='form_cursos'),
]