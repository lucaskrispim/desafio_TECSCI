from rest_framework.routers import DefaultRouter
from production.views.usina import UsinaViewSet
from production.views.inversor import InversorViewSet
from production.views.leitura import LeituraViewSet
from django.urls import path
from .views.analytics import (
    PotenciaMaxAPIView, TempMediaAPIView,
    GeracaoInversorAPIView, GeracaoUsinaAPIView
)

urlpatterns = []

router = DefaultRouter()
router.register(r'usinas', UsinaViewSet, basename='usina')
router.register(r'inversores', InversorViewSet, basename='inversor')
router.register(r'leituras', LeituraViewSet,   basename='leitura')

urlpatterns += router.urls

urlpatterns += [
    path('analytics/potencia-max/',    PotenciaMaxAPIView.as_view(),    name='pot_max'),
    path('analytics/temp-media/',      TempMediaAPIView.as_view(),      name='temp_media'),
    path('analytics/geracao-inversor/', GeracaoInversorAPIView.as_view(), name='ger_inv'),
    path('analytics/geracao-usina/',    GeracaoUsinaAPIView.as_view(),    name='ger_usina'),
]