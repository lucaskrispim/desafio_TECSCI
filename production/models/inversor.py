from django.db import models
from .usina import Usina

class Inversor(models.Model):
    usina = models.ForeignKey(
        Usina,
        on_delete=models.CASCADE,
        related_name="inversores",
        verbose_name="Usina"
    )
    identificador = models.CharField("Identificador", max_length=50)

    class Meta:
        verbose_name = "Inversor"
        verbose_name_plural = "Inversores"
        unique_together = ("usina", "identificador")

    def __str__(self):
        return f"{self.identificador} ({self.usina.nome})"
