from django.contrib import admin
from .models import Aluno


class AlunoModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'data_nascimento'
    ]


admin.site.register(Aluno, AlunoModelAdmin)