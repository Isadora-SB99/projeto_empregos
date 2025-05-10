from django.contrib import admin
from .models import Vaga, Candidato

# Register your models here.


@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'area', 'tipo_contrato', 'descricao')
    search_fields = ('nome',)
    list_filter = ('titulo',)


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'data_nascimento',
                    'genero', 'email', 'telefone', 'escolaridade')
    search_fields = ('nome',)
    list_filter = ('escolaridade',)
