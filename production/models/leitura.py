from django.db import models
from .inversor import Inversor

class Leitura(models.Model):
    inversor = models.ForeignKey(
        Inversor,
        on_delete=models.CASCADE,
        related_name="leituras",
        verbose_name="Inversor"
    )
    timestamp = models.DateTimeField("Data e Hora")
    potencia = models.FloatField("Potência (W)")
    temperatura = models.FloatField("Temperatura (°C)")

    class Meta:
        verbose_name = "Leitura"
        verbose_name_plural = "Leituras"
        ordering = ["-timestamp"]
        indexes = [
            models.Index(fields=["timestamp"]),
            models.Index(fields=["inversor", "timestamp"]),
        ]

    def __str__(self):
        ts = self.timestamp.isoformat(sep=" ")
        return f"Leitura {self.inversor.identificador} @ {ts}"
