import json
from django.core.management.base import BaseCommand, CommandError
from django.utils.dateparse import parse_datetime

from production.models import Usina, Inversor, Leitura

class Command(BaseCommand):
    help = "Seeda métricas a partir de um arquivo JSON"

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            "-f",
            required=True,
            help="Caminho para o arquivo metrics.json",
        )

    def handle(self, *args, **opts):
        path = opts["file"]
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise CommandError(f"Erro ao ler JSON: {e}")

        if not isinstance(data, list):
            self.stderr.write("JSON root não é uma lista; convertendo para lista de 1 elemento")
            data = [data]

        usina1, _ = Usina.objects.get_or_create(nome="Usina 1")
        usina2, _ = Usina.objects.get_or_create(nome="Usina 2")

        leituras = []
        total = len(data)
        for idx, entry in enumerate(data, 1):
            self.stdout.write(f"[{idx}/{total}] processando entrada: {entry}")

            pot = entry.get("potencia_ativa_watt")
            if pot is None:
                self.stderr.write(f"ERROR: 'potencia_ativa_watt' ausente ou nulo; pulando entrada")
                continue

            temp = entry.get("temperatura_celsius")
            if temp is None:
                self.stderr.write(f"ERROR: 'temperatura_celsius' ausente ou nulo; pulando entrada")
                continue

            dt_field = None
            try:
                dt_field = entry["datetime"]["$date"]
            except Exception:
                self.stderr.write(f"ERROR: campo 'datetime.$date' inválido ou ausente; pulando entrada")
                continue
            ts = parse_datetime(dt_field)
            if ts is None:
                self.stderr.write(f"ERROR: formato de data inválido ({dt_field}); pulando entrada")
                continue

            inv_id = entry.get("inversor_id")
            if inv_id is None:
                self.stderr.write(f"ERROR: 'inversor_id' ausente; pulando entrada")
                continue

            usina = usina1 if 1 <= inv_id <= 4 else usina2

            inversor, _ = Inversor.objects.get_or_create(
                usina=usina, identificador=str(inv_id)
            )

            leituras.append(
                Leitura(
                    inversor=inversor,
                    timestamp=ts,
                    potencia=pot,
                    temperatura=temp,
                )
            )

        if not leituras:
            self.stderr.write("Nenhuma leitura válida para inserir. Verifique os erros acima.")
            return

        Leitura.objects.bulk_create(leituras, batch_size=500)
        self.stdout.write(self.style.SUCCESS(
            f"Seed completo! {len(leituras)} leituras inseridas com sucesso."
        ))
