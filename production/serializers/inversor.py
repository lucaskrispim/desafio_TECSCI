from rest_framework import serializers
from production.models import Inversor

class InversorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inversor
        fields = ['id', 'usina', 'identificador']
        read_only_fields = ['id']