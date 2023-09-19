from rest_framework import viewsets, generics
from .models import Categoria, Usuario, Pedido, Produto, ItemPedido, Mesa
from .serializers import (
    CategoriaSerializer,
    UsuarioSerializer,
    PedidoSerializer,
    ProdutoSerializer,
    ItemPedidoSerializer,
    MesaSerializer,
    ListaPedidosMesaSerializer,
)


class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer


class ListaPedidosMesa(generics.ListAPIView):
    def get_queryset(self):
        queryset = Pedido.objects.filter(mesa=self.kwargs["pk"])
        return queryset

    serializer_class = ListaPedidosMesaSerializer


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


class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer
