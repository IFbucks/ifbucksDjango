from django.contrib import admin

from .models import Categoria, Carrinho, Pedido, Produto, Usuario

admin.site.register(Categoria)
admin.site.register(Carrinho)
admin.site.register(Pedido)
admin.site.register(Produto)
admin.site.register(Usuario)
