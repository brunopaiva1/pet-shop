from django.db import models

# Create your models here.

class Cliente(models.Model):
    cpf = models.CharField(max_length=11)
    nome_cliente = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    endereco = models.TextField(max_length=200)

    def __str__(self) -> str:
        return f'Cliente {self.cpf}'
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
