from django.db import models
from decimal import Decimal


class Categoria(models.Model):
    nome = models.CharField(max_length=100, default="Categoria")
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


def user_image_upload_to(instance, filename):
    return f"usuarios/{instance.cpf}/{filename}"


class Usuario(models.Model):
    CLIENTE = "Cliente"
    GARCOM = "Garçom"
    COZINHEIRO = "Cozinheiro"
    GERENTE = "Gerente"

    CARGO_CHOICES = (
        (CLIENTE, "Cliente"),
        (GARCOM, "Garçom"),
        (COZINHEIRO, "Cozinheiro"),
        (GERENTE, "Gerente"),
    )

    cpf = models.CharField(max_length=11, unique=True)
    cargo = models.CharField(max_length=255, choices=CARGO_CHOICES, default=CLIENTE)
    email = models.EmailField(null=True)
    nome = models.CharField(max_length=255, null=False, blank=False, default="Usuário")
    imagem = models.FileField(upload_to=user_image_upload_to, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def imagem_url(self):
        if self.imagem:
            return self.imagem.url
        return None


class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.numero} - " + "Ativa" if self.status else "Inativa"

    class Meta:
        verbose_name = "Mesa"
        verbose_name_plural = "Mesas"


class Carrinho(models.Model):
    mesa = models.ForeignKey(
        Mesa, on_delete=models.CASCADE, related_name="carrinhos", unique=True
    )
    usuario = models.ForeignKey(
        Usuario, on_delete=models.SET_NULL, null=True, related_name="carrinhos"
    )
    status = models.BooleanField(default=True)
    items_pedidos = models.ManyToManyField("Produto", through="Pedido")

    def __str__(self):
        return (
            "Carrinho da mesa " + str(self.mesa.numero) + " - " + "Ativo"
            if self.status
            else "Inativo"
        )

    def getTotal(self):
        total = Decimal("0.00")  # Inicialize o total como zero com precisão decimal

        # Percorra os itens no carrinho (relação através de Pedido)
        for pedido in self.pedidos.all():
            # Calcule o preço total do pedido (preço do produto multiplicado pela quantidade)
            pedido_total = pedido.produto.preco * Decimal(pedido.quantidade)
            total += pedido_total  # Adicione o total do pedido ao total geral

        return total  # Retorne o total como um objeto Decimal

    total = property(getTotal)

    class Meta:
        verbose_name = "Carrinho"
        verbose_name_plural = "Carrinhos"


def produto_image_upload_to(instance, filename):
    return f"usuarios/{instance.categoria}/{filename}"


class Produto(models.Model):
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=255)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="produtos"
    )
    imagem = models.FileField(upload_to=produto_image_upload_to, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def imagem_url(self):
        if self.imagem:
            return self.imagem.url
        return None


class Pedido(models.Model):
    carrinho = models.ForeignKey(
        Carrinho, on_delete=models.PROTECT, null=True, related_name="pedidos"
    )
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, null=True)
    hora_pedido = models.DateTimeField(auto_now_add=True)
    quantidade = models.IntegerField(default=1)
    entregue = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.carrinho} - {self.produto} - {self.quantidade}"

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
