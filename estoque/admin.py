from django.contrib import admin
from .models import Produto, PedidoReposicao

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade_atual', 'quantidade_minima', 'precisa_repor')
    search_fields = ('nome',)

@admin.register(PedidoReposicao)
class PedidoReposicaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'data_pedido', 'resolvido')
    list_filter = ('resolvido',)