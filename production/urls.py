from rest_framework.routers import DefaultRouter
from production.views.usina import UsinaViewSet
from production.views.inversor import InversorViewSet

router = DefaultRouter()
router.register(r'usinas', UsinaViewSet, basename='usina')
router.register(r'inversores', InversorViewSet, basename='inversor')

urlpatterns = router.urls
