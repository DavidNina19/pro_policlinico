from rest_framework import serializers
from .models import DetalleMedico
import requests

class DetalleMedicoSerializer(serializers.ModelSerializer):
    nomMed = serializers.SerializerMethodField()
    fecHora = serializers.SerializerMethodField()

    class Meta:
        model = DetalleMedico
        fields = ['numHor', 'fecHora', 'codMed', 'nomMed']

    def get_nomMed(self, obj):
        try:
            response = requests.get(f'http://getmedico:5000/listar/medico/{obj.codMed}/')
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and data:
                    return data[0]
            return "No encontrado"
        except Exception as e:
            return f"Error: {e}"

    def get_fecHora(self, obj):
        try:
            response = requests.get(f'http://gethorario:5000/listar/horario/{obj.numHor}/')  # Asegúrate del nombre del contenedor
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and data:
                    return data[0]
            return "No encontrado"
        except Exception as e:
            return f"Error: {e}"