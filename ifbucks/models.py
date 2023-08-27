from django.db import models

from django.db import models


class Pedidos(models.Model):
    mesa = models.IntegerField(default=0)
    usuario = models.ForeignKey("Usuario", on_delete=models.SET_NULL, null=True)
    status = models.BooleanField()
    hora_pedido = models.TimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["id"], name="unique_pedido_id"),
        ]

#  def __str__(self):
#        return self.nome

class Usuario(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    tipopessoa = models.ForeignKey("TipoPessoa", on_delete=models.CASCADE)
    email = models.EmailField(null=True)  # Note: Should be an email field

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["cpf", "id"], name="unique_usuario_cpf_id"),
        ]


class Produtos(models.Model):
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=255, default="1000")
    tipoProduto = models.ForeignKey(
        "TiposProdutos", on_delete=models.SET_NULL, null=True
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["id"], name="unique_produto_id"),
        ]


class TiposProdutos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["id"], name="unique_tipoproduto_id"),
        ]


class ItemPedido(models.Model):
    pedido = models.ForeignKey("Pedidos", on_delete=models.CASCADE)
    produto = models.ForeignKey("Produtos", on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)


class TipoPessoa(models.Model):
    descricao = models.CharField(max_length=1000)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["id"], name="unique_tipopessoa_id"),
        ]
