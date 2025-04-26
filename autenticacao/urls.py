from django.urls import path
from .views import registro, index

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('', index, name='index')
]
