from django import views
from django.contrib import admin
from django.urls import path, include
from pontos_turisticos.apis.viewsets import PontoTuristicoViewSet
from atracoes.apis.viewsets import AtracaoViewSet
from enderecos.apis.viewsets import EnderecoViewSet
from comentarios.apis.viewsets import ComentarioViewSet
from avaliacoes.apis.viewsets import AvaliacaoViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'pontoturistico', PontoTuristicoViewSet)
router.register(r'atracoes', AtracaoViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('admin/', admin.site.urls),


]
