from django.db import models

class Curriculo(models.Model):
    nome_completo = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.IntegerField()
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)