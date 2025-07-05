from rest_framework import serializers
from .models import Hora

class HoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hora
        fields = ['codHor', 'horaIni', 'horaFin']