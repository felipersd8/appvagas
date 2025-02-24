from django.contrib import admin
from .models import Profissional, Vaga

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'profissao', 'email')  # Campos que aparecem na listagem
    search_fields = ('nome', 'profissao', 'email')  # Permite busca por esses campos
    list_filter = ('profissao',)  # Adiciona filtros laterais

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'salario')  # Campos na listagem
    search_fields = ('titulo', 'descricao')  # Busca
    list_filter = ('salario',)  # Filtro por salário
