from django.contrib import admin

from .models import itemPedido
from .models import Pedidos
from .models import Produtos
from .models import Usuario
from .models import TipoPessoa
from .models import tipoProduto

admin.site.register(itemPedido)
admin.site.register(Pedidos)
admin.site.register(Produtos)
admin.site.register(Usuario)
admin.site.register(TipoPessoa)
admin.site.register(tipoProduto)