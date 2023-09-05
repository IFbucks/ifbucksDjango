from django.db import models



class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class TipoPessoa(models.Model):
    descricao = models.CharField(max_length=1000)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Tipo de Pessoa"
        verbose_name_plural = "Tipos de Pessoa"

class Usuario(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    tipopessoa = models.ForeignKey(TipoPessoa, on_delete=models.PROTECT)
    email = models.EmailField(null=True)
    nome = models.CharField(max_length=255, null=False, blank=False, default="Usuário")

    def __str__(self):
        return self.cpf

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class Pedido(models.Model):
    mesa = models.IntegerField(default=1)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField()
    hora_pedido = models.TimeField()

    def __str__(self):
        return f"{self.mesa} - {self.usuario_id} - {self.status} - {self.hora_pedido}"

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

class TipoProduto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Produto"
        verbose_name_plural = "Tipos de Produtos"

class Produto(models.Model):
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=255, default="aa")
    tipoProduto = models.ForeignKey(
        TipoProduto, on_delete=models.SET_NULL, null=True
    )
    imagem = models.ImageField(upload_to="prduto/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

class ItemPedido(models.Model):
    pedido_id = models.ForeignKey(Pedido, on_delete=models.PROTECT, null=True)
    produto_id = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.pedido_id} - {self.produto_id} - {self.quantidade}"

    class Meta:
        verbose_name = "Item Pedido"
        verbose_name_plural = "Itens Pedido"
