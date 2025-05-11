from django.db import models

class Usina(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Usina"
        verbose_name_plural = "Usinas"

    def __str__(self):
        return self.nome