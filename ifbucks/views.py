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

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@permission_classes((IsAuthenticated,))
class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer


@permission_classes((IsAuthenticated,))
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


@permission_classes((IsAuthenticated,))
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


@permission_classes((IsAuthenticated,))
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


@permission_classes((IsAuthenticated,))
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


@permission_classes((IsAuthenticated,))
class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer


@permission_classes((IsAuthenticated,))
class PedidosMesa(generics.ListAPIView):
    """Lista todos os pedidos relacionados a uma mesa"""

    serializer_class = PedidoSerializer

    def get_queryset(self):
        mesa = self.kwargs["pk"]
        return Pedido.objects.filter(carrinho__mesa=mesa)


@permission_classes((IsAuthenticated,))
class CarrinhoMesa(generics.ListAPIView):
    """Lista todos o carrinho relacionados a uma mesa"""

    serializer_class = CarrinhoSerializer

    def get_queryset(self):
        mesa = self.kwargs["pk"]
        return Carrinho.objects.filter(mesa=mesa)


@permission_classes((IsAuthenticated,))
class ProdutosCategoria(generics.ListAPIView):
    """Lista todos os produtos relacionados a uma categoria"""

    serializer_class = ProdutoSerializer

    def get_queryset(self):
        categoria = self.kwargs["pk"]  # pk é o nome da categoria
        return Produto.objects.filter(categoria__nome=categoria)
