from rest_framework import serializers
from production.models import Usina

class UsinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usina
        fields = ['id', 'nome']