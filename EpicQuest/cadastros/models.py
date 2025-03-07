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