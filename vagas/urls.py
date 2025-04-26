from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.index, name="vagas"),
    path('', views.create_job_post, name='create'),
    path('', views.list_job_posts, name='list'),

]
urlpatterns += [
    path('example/', TemplateView.as_view(template_name='example_template.html'), name='example'),
]