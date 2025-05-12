from rest_framework.routers import DefaultRouter
from production.views.usina import UsinaViewSet
# (importe outros viewsets quando estiver prontos)

router = DefaultRouter()
router.register(r'usinas', UsinaViewSet, basename='usina')

urlpatterns = router.urls
