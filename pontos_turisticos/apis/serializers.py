from rest_framework import serializers
from pontos_turisticos.models import PontoTuristico


class PontoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao')
