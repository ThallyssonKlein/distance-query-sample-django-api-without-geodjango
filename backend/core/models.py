from django.db import models

from django.contrib import admin

class Loja(models.Model):
    empresa = models.CharField(max_length=20)
    lojista = models.CharField(max_length=50)
    loja = models.CharField(max_length=20)
    nome = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=4)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    ativo = models.BooleanField(default=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude  = models.DecimalField(max_digits=10, decimal_places=7)

admin.site.register(Loja)