from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from receitas.serializers import *

# Viewset da Receita
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

# Viewset da Despesa
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

# Viewset do Resumo

class ResumoViewSet(APIView):
    """
    Visualizar Resumo por Ano/Mês
    """
    def get(self, request, ano, mes):
        valor_total_receitas = Receita.objects.filter(data__year=ano, data__month=mes).aggregate(
            Sum('valor'))['valor__sum'] or 0
        valor_total_despesas = Despesa.objects.filter(data__year=ano, data__month=mes).aggregate(
            Sum('valor'))['valor__sum'] or 0
        despesa_por_categoria = Despesa.objects.filter(data__year=ano, data__month=mes).values(
            'categoria').annotate(Sum('valor'))
        saldo_final = valor_total_receitas - valor_total_despesas

        for d in despesa_por_categoria:
            d['valor'] = d['valor__sum']
            del d['valor__sum']

        return Response({
            'Receita/Mês': valor_total_receitas,
            'Despesa/Mês': valor_total_despesas,
            'Categoria/Mês': despesa_por_categoria,
            'Saldo Final/Mês': saldo_final
        })

