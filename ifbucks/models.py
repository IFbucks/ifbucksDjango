from django.db import models


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

    TIPOS_PESSOAS = (
        (CLIENTE, "Cliente"),
        (GARCOM, "Garçom"),
        (COZINHEIRO, "Cozinheiro"),
        (GERENTE, "Gerente"),
    )

    cpf = models.CharField(max_length=11, unique=True)
    cargo = models.CharField(max_length=255, choices=TIPOS_PESSOAS, default=CLIENTE)
    email = models.EmailField(null=True)
    nome = models.CharField(max_length=255, null=False, blank=False, default="Usuário")
    imagem = models.ImageField(upload_to=user_image_upload_to, blank=True, null=True)

    def __str__(self):
        return self.cpf

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def imagem_url(self):
        if self.imagem:
            return self.imagem.url
        return None


class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.numero} - {self.status}"

    class Meta:
        verbose_name = "Mesa"
        verbose_name_plural = "Mesas"


class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.PROTECT, related_name="pedidos")
    usuario = models.ForeignKey(
        Usuario, on_delete=models.SET_NULL, null=True, related_name="pedidos"
    )
    status = models.BooleanField()
    hora_pedido = models.DateTimeField(auto_now_add=True)
    items_pedidos = models.ManyToManyField("Produto", through="ItemPedido")

    def __str__(self):
        return f"{self.mesa} - {self.usuario} - {self.status} - {self.hora_pedido}"

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"


def produto_image_upload_to(instance, filename):
    return f"usuarios/{instance.categorio}/{filename}"


class Produto(models.Model):
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to=produto_image_upload_to, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def imagem_url(self):
        if self.imagem:
            return self.imagem.url
        return None


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.pedido} - {self.produto} - {self.quantidade}"

    class Meta:
        verbose_name = "Item Pedido"
        verbose_name_plural = "Itens Pedido"
