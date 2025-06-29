from rest_framework import serializers
from .models import Hora

class HoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hora
        fields = ['codHora', 'horaIni', 'horaFin']
        read_only_fields = ['codHora']  # codHora es autoincrementable y no se envía en POST