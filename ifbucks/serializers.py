from rest_framework import serializers
from .models import (
    Categoria,
    TipoPessoa,
    Usuario,
    Pedido,
    TipoProduto,
    Produto,
    ItemPedido,
)


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class TipoPessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPessoa
        fields = "__all__"


class UsuarioSerializer(serializers.ModelSerializer):
    imagem_url = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = "__all__"

    def get_imagem_url(self, obj):
        return obj.imagem_url()


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"


class TipoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProduto
        fields = "__all__"


class ProdutoSerializer(serializers.ModelSerializer):
    imagem_url = serializers.SerializerMethodField()

    class Meta:
        model = Produto
        fields = "__all__"

    def get_imagem_url(self, obj):
        return obj.imagem_url()


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = "__all__"
