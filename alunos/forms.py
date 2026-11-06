from django import forms
from django.core.exceptions import ValidationError

from .models import Aluno


class AlunoForm(forms.ModelForm):
  class Meta:
    model = Aluno
    fields = ['nome', 'email', 'matricula']
    widgets = {
      'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Aluno'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'matricula': forms.TextInput(attrs={'class': 'form-control'}),
    }
    labels = {
      'nome': 'Nome do Aluno',
      'email': 'E-mail',
      'matricula': 'Matrícula',
    }

  def clean_matricula(self):
    matricula = self.cleaned_data['matricula']

    if len(matricula) != 8:
      raise ValidationError('Matrícula deve ter 8 dígitos')

    return matricula
