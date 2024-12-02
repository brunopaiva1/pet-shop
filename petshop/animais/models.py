from django.db import models

from cliente.models import Cliente

# Create your models here.

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    idade = models.CharField(max_length=30)
    peso = models.FloatField()
<<<<<<< HEAD
    qtd_vacinas = models.IntegerField(default=0)
=======
    qtd_vacinas = models.IntegerField()
>>>>>>> origin/main
    dono = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
def __str__(self):
        return f'Animal {self.nome}'
    
class Meta:
    verbose_name = "Animal"
    verbose_name_plural = "Animais"    