from rest_framework import serializers
from .models import *

class ReceitaSerial(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = "__all__"

class DespesaSerial (serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = "__all__"