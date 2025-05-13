from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max, Avg
from django.db.models.functions import TruncDate
from django.shortcuts import get_object_or_404
from production.models import Leitura, Inversor, Usina
from datetime import timedelta

class PotenciaMaxAPIView(APIView):
    def get(self, request):
        inv_id = request.query_params.get("inversor_id")
        start = request.query_params.get("data_inicio")
        end   = request.query_params.get("data_fim")
        if not all([inv_id, start, end]):
            return Response(
                {"detail": "Parâmetros inversor_id, data_inicio e data_fim são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST
            )
        qs = (
            Leitura.objects
            .filter(inversor_id=inv_id, timestamp__date__gte=start, timestamp__date__lte=end)
            .annotate(date=TruncDate("timestamp"))
            .values("date")
            .annotate(max_potencia=Max("potencia"))
            .order_by("date")
        )
        return Response(list(qs))


class TempMediaAPIView(APIView):
    def get(self, request):
        inv_id = request.query_params.get("inversor_id")
        start = request.query_params.get("data_inicio")
        end   = request.query_params.get("data_fim")
        if not all([inv_id, start, end]):
            return Response(
                {"detail": "Parâmetros inversor_id, data_inicio e data_fim são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST
            )
        qs = (
            Leitura.objects
            .filter(inversor_id=inv_id, timestamp__date__gte=start, timestamp__date__lte=end)
            .annotate(date=TruncDate("timestamp"))
            .values("date")
            .annotate(temp_media=Avg("temperatura"))
            .order_by("date")
        )
        return Response(list(qs))


def _calcula_geracao(readings):
    """
    readings: lista de leituras ordenada por timestamp
    Retorna energia em Wh via regra do trapézio
    """
    energy = 0.0
    for prev, curr in zip(readings, readings[1:]):
        dt = (curr.timestamp - prev.timestamp).total_seconds() / 3600
        avg_p = (curr.potencia + prev.potencia) / 2
        energy += avg_p * dt
    return energy


class GeracaoInversorAPIView(APIView):
    def get(self, request):
        inv_id = request.query_params.get("inversor_id")
        start = request.query_params.get("data_inicio")
        end   = request.query_params.get("data_fim")
        if not all([inv_id, start, end]):
            return Response(
                {"detail": "Parâmetros inversor_id, data_inicio e data_fim são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST
            )

        inversor = get_object_or_404(Inversor, pk=inv_id)
        readings = list(
            Leitura.objects
            .filter(inversor=inversor, timestamp__date__gte=start, timestamp__date__lte=end)
            .order_by("timestamp")
        )
        if len(readings) < 2:
            return Response({"inversor": inv_id, "geracao_wh": 0.0})

        energy = _calcula_geracao(readings)
        return Response({"inversor": inv_id, "geracao_wh": energy})


class GeracaoUsinaAPIView(APIView):
    def get(self, request):
        usina_id = request.query_params.get("usina_id")
        start = request.query_params.get("data_inicio")
        end   = request.query_params.get("data_fim")
        if not all([usina_id, start, end]):
            return Response(
                {"detail": "Parâmetros usina_id, data_inicio e data_fim são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST
            )

        usina = get_object_or_404(Usina, pk=usina_id)
        total_energy = 0.0
        for inv in usina.inversores.all():
            readings = list(
                inv.leituras
                .filter(timestamp__date__gte=start, timestamp__date__lte=end)
                .order_by("timestamp")
            )
            if len(readings) >= 2:
                total_energy += _calcula_geracao(readings)

        return Response({"usina": usina_id, "geracao_wh": total_energy})
