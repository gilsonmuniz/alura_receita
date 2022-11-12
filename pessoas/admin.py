from django.contrib import admin
from .models import Pessoa


class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',) # Campos que podem ser pesquisados na barra de pesquisa (é necessário colocar ',' por ser uma tupla)
    list_per_page = 20 # número de itens por página

admin.site.register(Pessoa, ListandoPessoas)