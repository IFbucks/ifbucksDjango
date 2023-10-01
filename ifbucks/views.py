from rest_framework import viewsets, generics
from .models import Categoria, Usuario, Pedido, Produto, Carrinho, Mesa
from .serializers import (
    CategoriaSerializer,
    UsuarioSerializer,
    PedidoSerializer,
    ProdutoSerializer,
    CarrinhoSerializer,
    MesaSerializer,
)


class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer


class PedidosMesa(generics.ListAPIView):
    """Lista todos os pedidos relacionados a uma mesa"""

    serializer_class = PedidoSerializer

    def get_queryset(self):
        mesa = self.kwargs["pk"]
        return Pedido.objects.filter(carrinho__mesa=mesa)


class CarrinhoMesa(generics.ListAPIView):
    """Lista todos o carrinho relacionados a uma mesa"""

    serializer_class = CarrinhoSerializer

    def get_queryset(self):
        mesa = self.kwargs["pk"]
        return Carrinho.objects.filter(mesa=mesa)


class ProdutosCategoria(generics.ListAPIView):
    """Lista todos os produtos relacionados a uma categoria"""

    serializer_class = ProdutoSerializer

    def get_queryset(self):
        categoria = self.kwargs["pk"]
        return Produto.objects.filter(categoria=categoria)
