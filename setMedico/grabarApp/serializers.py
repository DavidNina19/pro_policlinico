from rest_framework import serializers
from .models import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['codMed', 'nomMed', 'especial', 'estado']
        read_only_fields = ['codMed']  # codMed es autoincrementable