from rest_framework import serializers
from enderecos.models import Endereco


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'linha1', 'linha2', 'cidade', 'estado',
                  'pais', 'latitude', 'longitude')
