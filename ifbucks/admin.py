from django.contrib import admin

from .models import ItemPedido
from .models import Pedido
from .models import Produto
from .models import Usuario
from .models import TipoPessoa
from .models import TipoProduto

admin.site.register(ItemPedido)
admin.site.register(Pedido)
admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(TipoPessoa)
admin.site.register(TipoProduto)