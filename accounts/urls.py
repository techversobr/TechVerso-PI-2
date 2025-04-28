from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [	
    path('register', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', RedirectView.as_view(pattern_name='register', permanent=False), name='account_redirect'),

] 