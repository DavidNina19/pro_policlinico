from rest_framework import serializers
from .models import Analisis

class AnalisisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analisis
        fields = ['codTipo', 'tipoAnalisis']
        read_only_fields = ['codTipo']  # codMed es autoincrementable