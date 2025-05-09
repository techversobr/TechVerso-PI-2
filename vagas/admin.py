# filepath: c:\Users\Usuario\Desktop\PI\TechVerso\vagas\admin.py
from django.contrib import admin
from .models import JobPost

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'location', 'salary', 'contract_type')
