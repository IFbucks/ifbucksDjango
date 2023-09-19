from django.contrib import admin

from .models import Categoria, ItemPedido, Pedido, Produto, Usuario

admin.site.register(Categoria)
admin.site.register(ItemPedido)
admin.site.register(Pedido)
admin.site.register(Produto)
admin.site.register(Usuario)
