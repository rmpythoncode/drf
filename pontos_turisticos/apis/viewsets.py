from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import PontoTuristico
from pontos_turisticos.apis.serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer