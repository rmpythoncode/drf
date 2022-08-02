from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from atracoes.apis.serializers import AtracaoSerializer


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
