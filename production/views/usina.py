from rest_framework import viewsets
from production.models import Usina
from production.serializers.usina import UsinaSerializer

class UsinaViewSet(viewsets.ModelViewSet):
    """
    CRUD completo de Usina:
      - list:   GET  /api/usinas/
      - retrieve: GET  /api/usinas/{pk}/
      - create: POST /api/usinas/
      - update: PUT  /api/usinas/{pk}/
      - partial_update: PATCH /api/usinas/{pk}/
      - destroy: DELETE /api/usinas/{pk}/
    """
    queryset = Usina.objects.all()
    serializer_class = UsinaSerializer
