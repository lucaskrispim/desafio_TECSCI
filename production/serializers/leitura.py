from rest_framework import serializers
from production.models import Leitura

class LeituraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leitura
        fields = ['id', 'inversor', 'timestamp', 'potencia', 'temperatura']
        read_only_fields = ['id']
