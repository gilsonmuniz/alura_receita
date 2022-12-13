from django.contrib import admin
from .models import Receita


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada') # Campos que aparecem na lista de receitas
    list_display_links = ('id', 'nome_receita') # Campos que possuem link para entrar na receita
    search_fields = ('nome_receita',) # Campos que podem ser pesquisados na barra de pesquisa (é necessário colocar ',' por ser uma tupla)
    list_filter = ('categoria',) # Filtro de categoria
    list_editable = ('publicada',) # Permite o checkbox na lista de receitas no campo 'publicada'
    list_per_page = 20 # número de itens por página


admin.site.register(Receita, ListandoReceitas)
