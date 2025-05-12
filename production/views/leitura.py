from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view
from production.models import Leitura
from production.serializers.leitura import LeituraSerializer

@extend_schema_view(
    list=extend_schema(
        summary="Listar Leituras",
        description="Retorna todas as leituras registradas (filtráveis por inversor e intervalo de timestamp)",
        tags=['Leituras'],
    ),
    retrieve=extend_schema(
        summary="Detalhar Leitura",
        description="Retorna uma única leitura pelo ID",
        tags=['Leituras'],
    ),
    create=extend_schema(
        summary="Criar Leitura",
        description="Adiciona uma nova leitura para um inversor",
        tags=['Leituras'],
        request=LeituraSerializer,
        responses={201: LeituraSerializer},
    ),
    update=extend_schema(
        summary="Atualizar Leitura (PUT)",
        description="Substitui completamente os dados de uma leitura existente",
        tags=['Leituras'],
    ),
    partial_update=extend_schema(
        summary="Atualizar Leitura (PATCH)",
        description="Atualiza parcialmente os campos de uma leitura",
        tags=['Leituras'],
    ),
    destroy=extend_schema(
        summary="Excluir Leitura",
        description="Remove uma leitura pelo ID",
        tags=['Leituras'],
    ),
)
class LeituraViewSet(viewsets.ModelViewSet):
    """
    CRUD de Leituras:
      • GET    /api/leituras/         → lista
      • POST   /api/leituras/         → cria
      • GET    /api/leituras/{id}/    → detalhe
      • PUT    /api/leituras/{id}/    → atualiza
      • PATCH  /api/leituras/{id}/    → atualiza parcialmente
      • DELETE /api/leituras/{id}/    → exclui
    """
    queryset = Leitura.objects.all()
    serializer_class = LeituraSerializer
    filterset_fields = {
        'inversor': ['exact'],
        'timestamp': ['gte', 'lte'],
    }
