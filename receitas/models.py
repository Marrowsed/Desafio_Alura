from django.db import models

class Receita(models.Model):
    descricao = models.CharField(max_length=200, unique_for_month="data")
    valor = models.FloatField()
    data = models.DateField()

class Despesa(models.Model):
    OUTRAS = "Outras"
    ESCOLHAS = (
        ("A", "Alimentação"),
        ("S", "Saúde"),
        ("M", "Moradia"),
        ("T", "Transporte"),
        ("E", "Educação"),
        ("L", "Lazer"),
        ("I", "Imprevistos"),
        ("O", "Outras")
    )
    descricao = models.CharField(max_length=200, unique_for_month="data")
    categoria = models.CharField(max_length=200, blank=False, choices=ESCOLHAS, default=OUTRAS)
    valor = models.FloatField()
    data = models.DateField()
