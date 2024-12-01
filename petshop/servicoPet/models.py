from django.db import models
from cliente.models import Cliente
from animais.models import Animal

# Create your models here.

class ServicoPet(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    horarioEntrada = models.DateTimeField()
    horarioSaida = models.DateTimeField()
    tipoServico = models.CharField(max_length=50, choices=[
        ('banho', 'Banho'),
        ('tosa', 'Tosa'),
        ('banho e tosa', 'Banho e Tosa')
    ])
    
    def __str__(self):
        return f'ServicoPet {self.cliente}'
    
    class Meta:
        verbose_name = "ServicoPet"
        verbose_name_plural = "ServicosPet"