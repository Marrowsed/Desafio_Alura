from django.db import models

class Receita(models.Model):
    descricao = models.CharField(max_length=200, unique_for_month="data")
    valor = models.FloatField()
    data = models.DateField()

class Despesa(models.Model):
    descricao = models.CharField(max_length=200, unique_for_month="data")
    valor = models.FloatField()
    data = models.DateField()
