from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view
from production.models import Inversor
from production.serializers.inversor import InversorSerializer

@extend_schema_view(
    list=extend_schema(
        summary="Listar inversores",
        description="Retorna todos os inversores cadastrados",
        tags=['Inversores'],
    ),
    retrieve=extend_schema(
        summary="Detalhar inversor",
        description="Retorna um único inversor pelo ID",
        tags=['Inversores'],
    ),
    create=extend_schema(
        summary="Criar inversor",
        description="Cria um novo inversor associado a uma usina",
        tags=['Inversores'],
        request=InversorSerializer,
        responses={201: InversorSerializer},
    ),
    update=extend_schema(
        summary="Atualizar inversor (PUT)",
        description="Substitui completamente um inversor existente",
        tags=['Inversores'],
    ),
    partial_update=extend_schema(
        summary="Atualizar inversor (PATCH)",
        description="Atualiza parcialmente os campos de um inversor",
        tags=['Inversores'],
    ),
    destroy=extend_schema(
        summary="Excluir inversor",
        description="Remove um inversor pelo ID",
        tags=['Inversores'],
    ),
)
class InversorViewSet(viewsets.ModelViewSet):
    """
    ViewSet para CRUD de Inversor:
      • GET    /api/inversores/         → lista
      • POST   /api/inversores/         → cria
      • GET    /api/inversores/{id}/    → detalhe
      • PUT    /api/inversores/{id}/    → atualiza
      • PATCH  /api/inversores/{id}/    → atualiza parcialmente
      • DELETE /api/inversores/{id}/    → exclui
    """
    queryset = Inversor.objects.all()
    serializer_class = InversorSerializer
    filterset_fields = ['usina', 'identificador']
