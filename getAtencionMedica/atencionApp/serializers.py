from rest_framework import serializers
from .models import AtencionMedica
import requests

class AtencionMedicaSerializer(serializers.ModelSerializer):
    codCita = serializers.SerializerMethodField()
    id_receta = serializers.SerializerMethodField()
    codAnalisis = serializers.SerializerMethodField()

    class Meta:
        model = AtencionMedica
        fields = ['codAte', 'codCita', 'id_receta','codAnalisis', 'diagnostico', 'tratamiento', 't_stamp']

    def get_codCita(self, obj):
        try:
            response = requests.get(f'http://getcitamedica:5000/get/cita/?codCita={obj.codCita}/')
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and data:
                    return data[0]
            return "No encontrado"
        except Exception as e:
            return f"Error: {e}"

    def get_id_receta(self, obj):
        try:
            response = requests.get(f'http://detallereceta:5000/listar/detallereceta?id_receta={obj.id_receta}/')  # Asegúrate del nombre del contenedor
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and data:
                    return data[0]
            return "No encontrado"
        except Exception as e:
            return f"Error: {e}"
        
    def get_codAnalisis(self, obj):
        try:
            response = requests.get(f'http://detalleanalisis:5000/listar/detalleanalisis/?codAnalisis={obj.codAnalisis}') # Usando codAnalisis 
            response.raise_for_status() 
            data = response.json()
            
            if isinstance(data, list) and data:
                if isinstance(data[0], dict):
                    return {
                        'codAnalisis': data[0].get('codAnalisis', 'No disponible'),
                        'codTipo': data[0].get('codTipo', 'No disponible')
                    }
            return {'codAnalisis': 'No encontrado', 'codTipo': 'No encontrado'}
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener codAnalisis y codTipo para codAnalisis {obj.codAnalisis}: {e}")
            return {'codAnalisis': 'Error al cargar', 'codTipo': 'Error al cargar'}
        except Exception as e:
            print(f"Error inesperado al obtener codAnalisis y codTipo: {e}")
            return {'codAnalisis': 'Error inesperado', 'codTipo': 'Error inesperado'}