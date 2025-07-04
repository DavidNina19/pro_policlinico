# app_name/serializers.py
from rest_framework import serializers
from .models import Horario # Asegúrate de importar Horario
class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        # Asume que 'fecHora' es un campo de tu modelo Horario.
        # Si Horario tiene otros campos que quieres exponer, agrégalos aquí.
        fields = ['fecHora', 'numHor'] # Agregué 'numHor' también, asumiendo que quieres devolverlo.