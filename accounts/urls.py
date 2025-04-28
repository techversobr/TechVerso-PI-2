from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from .views import CustomLoginView


urlpatterns = [	
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', RedirectView.as_view(pattern_name='register', permanent=False), name='account_redirect'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

] 