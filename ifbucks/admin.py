from django.contrib import admin

from .models import ItemPedido
from .models import Pedidos
from .models import Pedidos
from .models import Usuario
from .models import TipoPessoa
from .models import TiposProdutos

admin.site.register(ItemPedido)
admin.site.register(Pedidos)
admin.site.register(Usuario)
admin.site.register(TipoPessoa)
admin.site.register(TiposProdutos)