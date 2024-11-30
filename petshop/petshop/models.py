from django.db import models

class PetShopModel(models.Model):

    animal = models.CharField(max_length=140)
    nome = models.CharField(max_length=140)
