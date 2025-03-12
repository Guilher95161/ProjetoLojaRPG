from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits = 10, decimal_places = 2)
    estoque = models.IntegerField()
    lancamento = models.DateField()
    categorias = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.nome
    
class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)
    precoTotal = models.DecimalField(max_digits = 10, decimal_places = 2)
    dataCompra = models.DateField()

    def __str__(self):
        return f"Compra {self.id} de {self.usuario}"

class ItemCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete = models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete= models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.jogo.nome}"

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    nota = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    comentario = models.TextField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação de {self.usuario} para {self.jogo.nome}"