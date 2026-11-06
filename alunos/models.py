from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100, null=False)
    matricula = models.CharField(max_length=8, null=False, unique=True)
    email = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'aluno'
        ordering = ['nome']

class Solicitacao(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    descricao = models.TextField(max_length=8, null=False)
    data = models.DateTimeField(auto_now_add=True, null=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='solicitacoes')

    class Meta:
        db_table = 'solicitacao'
        ordering = ['-data']