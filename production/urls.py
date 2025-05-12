from rest_framework.routers import DefaultRouter
from production.views.usina import UsinaViewSet
from production.views.inversor import InversorViewSet
from production.views.leitura import LeituraViewSet

router = DefaultRouter()
router.register(r'usinas', UsinaViewSet, basename='usina')
router.register(r'inversores', InversorViewSet, basename='inversor')
router.register(r'leituras', LeituraViewSet,   basename='leitura')

urlpatterns = router.urls
