from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    CANDIDATO = 'Candidato'
    RECRUTADOR = 'Recrutador'
    TIPOS_USUARIO = [
        (CANDIDATO, 'Candidato'),
        (RECRUTADOR, 'Recrutador'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    tipo_usuario = models.CharField(max_length=10, choices=TIPOS_USUARIO, default=CANDIDATO)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.CharField(max_length=500, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    curriculo = models.FileField(upload_to='curriculos/', null=True, blank=True)

    def __str__(self):
        return self.user.username

