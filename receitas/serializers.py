from rest_framework import serializers
from .models import *

#Serializer de Receita
class ReceitaSerial(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = "__all__"


#Serializer de Despeza
class DespesaSerial(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = "__all__"

#Serializer de Resumo

