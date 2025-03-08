from django.db import models

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
   # usuario = models.ForeignKey() Vou ver se uso o usuário que está logado ou uso Perfil ou criar um Cliente
    precoTotal = models.DecimalField(max_digits = 10, decimal_places = 2)
    dataCompra = models.DateField()

class ItemCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete = models.PROTECT)
    #usuario = models.ForeignKey() Vou ver se uso o usuário que está logado ou uso Perfil ou criar um Cliente, pra representar o usuário
    quantidade = models.IntegerField()
    