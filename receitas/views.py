from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from receitas.serializers import *


class ReceitaViewSet(viewsets.ModelViewSet):
    """
    Visualizar as Receitas
    """
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerial
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['descricao']

class ReceitaAnoMesViewSet(viewsets.ModelViewSet):
    """
    Visualizar por Ano/Mês
    """

    serializer_class = ReceitaSerial

    def get_queryset(self):
        ano = self.kwargs['ano']
        mes = self.kwargs['mes']
        return Receita.objects.filter(data__year=ano, data__month=mes)


class DespesaViewSet(viewsets.ModelViewSet):
    """
    Visualizar as Despesas
    """
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerial
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['descricao']



class DespesaAnoMesViewSet(viewsets.ModelViewSet):
    """
    Visualizar por Ano/Mês
    """

    serializer_class = ReceitaSerial

    def get_queryset(self):
        ano = self.kwargs['ano']
        mes = self.kwargs['mes']
        return Despesa.objects.filter(data__year=ano, data__month=mes)