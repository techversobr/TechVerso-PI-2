from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views
from autenticacao import views
from vagas import views as vagas_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/', include('allauth.urls')),
    path('register/', include('accounts.urls')),
    path('autenticacao/', include('autenticacao.urls')),
    path('vagas/', include('vagas.urls')),
    path('cursos/', include('cursos.urls')),
    path('sobre/', include('sobre.urls')),
    path("faq/", include("faq.urls")),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('create/', vagas_views.create_job_post, name='create'),
    path('list/', vagas_views.list_job_posts, name='list'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
