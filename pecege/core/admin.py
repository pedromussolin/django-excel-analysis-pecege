from django.contrib import admin
from .models import Pessoa


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_nascimento', 'ativo', 'valor')
    list_filter = ('ativo',)
    search_fields = ('nome', 'email')

