from django import forms
from django.contrib.auth.models import User
from .models import Usuario

TIPOS_USUARIO = [
    ('CANDIDATO', 'Candidato'),
    ('EMPREGADOR', 'Recrutador'),
    # Adicione outros tipos conforme necessário
]

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    tipo_usuario = forms.ChoiceField(choices=TIPOS_USUARIO, required=True)
    data_nascimento = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)), required=True)
    telefone = forms.CharField(max_length=15, required=False)
    endereco = forms.CharField(max_length=500, required=False)
    descricao = forms.CharField(widget=forms.Textarea, required=False)
    curriculo = forms.FileField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()

        usuario_complementar = Usuario.objects.create(
            user=user,  # A FK para User é preenchida automaticamente
            tipo_usuario=self.cleaned_data['tipo_usuario'],
            data_nascimento=self.cleaned_data['data_nascimento'],
            telefone=self.cleaned_data['telefone'],
            endereco=self.cleaned_data['endereco'],
            descricao=self.cleaned_data['descricao'],
            curriculo=self.cleaned_data['curriculo']
        )
        return user
