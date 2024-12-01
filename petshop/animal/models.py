from django.db import models
from cliente.models import Cliente

# Create your models here.

class Animal(models.Model):
    nome_animal = models.CharField(max_length=50)
    raca = models.CharField(max_length=30)
    idade = models.CharField(max_length=30)
    peso = models.FloatField()
    qtd_vacinas = models.IntegerField()
    dono_do_animal = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f'Animal {self.nome_animal}'
    
    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"
