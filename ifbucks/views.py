from rest_framework import viewsets
from .models import (
    Categoria,
    TipoPessoa,
    Usuario,
    Pedido,
    TipoProduto,
    Produto,
    ItemPedido,
)
from .serializers import (
    CategoriaSerializer,
    TipoPessoaSerializer,
    UsuarioSerializer,
    PedidoSerializer,
    TipoProdutoSerializer,
    ProdutoSerializer,
    ItemPedidoSerializer,
)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class TipoPessoaViewSet(viewsets.ModelViewSet):
    queryset = TipoPessoa.objects.all()
    serializer_class = TipoPessoaSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class TipoProdutoViewSet(viewsets.ModelViewSet):
    queryset = TipoProduto.objects.all()
    serializer_class = TipoProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer
