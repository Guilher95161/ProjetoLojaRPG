from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Jogo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits = 10, decimal_places = 2)
    estoque = models.IntegerField()
    lancamento = models.DateField()

    def __str__(self):
        return self.nome
    
class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete= models.PROTECT)
    precoTotal = models.DecimalField(max_digits = 10, decimal_places = 2)
    dataCompra = models.DateField()

    def __str__(self):
        return f"Compra {self.id} de {self.usuario}"

class ItemCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete = models.PROTECT)
    jogo = models.ForeignKey(Jogo, on_delete= models.PROTECT)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.jogo.nome}"
    