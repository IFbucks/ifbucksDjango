from rest_framework import serializers
from .models import Categoria, Usuario, Mesa, Pedido, Produto, ItemPedido


class ListaPedidosMesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = "__all__"


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = "__all__"
