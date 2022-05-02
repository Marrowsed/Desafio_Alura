from django.shortcuts import render
from rest_framework import viewsets

from receitas.serializers import *


class ReceitaViewSet(viewsets.ModelViewSet):
    """
    Visualizar as Receitas
    """
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerial


class DespesaViewSet(viewsets.ModelViewSet):
    """
    Visualizar as Despesas
    """
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerial
