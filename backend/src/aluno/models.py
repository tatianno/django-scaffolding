from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


class Aluno(ExportModelOperationsMixin('aluno'), models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self) -> str:
        return self.nome
