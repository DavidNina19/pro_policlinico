# app_name/serializers.py
from rest_framework import serializers
from .models import DetalleHora # Asegúrate de importar el nuevo modelo
import requests
class DetalleHoraSerializer(serializers.ModelSerializer):
    # Campos que vienen de microservicios externos
    nomMed = serializers.SerializerMethodField()
    fecHora = serializers.SerializerMethodField()
    hora = serializers.SerializerMethodField() # Para el detalle del horario específico

    class Meta:
        model = DetalleHora
        # Incluye todos los campos del modelo DetalleHora y los campos obtenidos
        fields = ['numHor', 'codMed', 'codHor', 'consul', 'estado', 'nomMed', 'fecHora', 'hora']
        read_only_fields = ['nomMed', 'fecHora', 'hora'] # Estos no se envían al crear/actualizar

    def get_nomMed(self, obj):
        try:
            # Recomiendo encarecidamente usar ?codMed={obj.codMed} si codMed es el ID.
            # Si tu API de medico espera ?nomMed={valor_del_codigo}, entonces manténlo.
            response = requests.get(f'http://getmedico:5000/listar/medico/?codMed={obj.codMed}') # Usando codMed como sugerencia
            response.raise_for_status() 
            data = response.json()
            
            if isinstance(data, list) and data:
                # Asumimos que la API devuelve un diccionario como {'nomMed': 'Roberto', 'especialidad': 'Cardiología'}
                if isinstance(data[0], dict):
                    return {
                        'nombre': data[0].get('nomMed', 'No disponible'),
                        'especialidad': data[0].get('especial', 'No disponible') # Asume que el campo se llama 'especialidad'
                    }
            return {'nombre': 'No encontrado', 'especialidad': 'No encontrado'}
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener nomMed y especialidad para codMed {obj.codMed}: {e}")
            return {'nombre': 'Error al cargar', 'especialidad': 'Error al cargar'}
        except Exception as e:
            print(f"Error inesperado al obtener nomMed y especialidad: {e}")
            return {'nombre': 'Error inesperado', 'especialidad': 'Error inesperado'}

    def get_fecHora(self, obj):
        try:
            # Usando numHora={obj.numHor} como lo definiste
            response = requests.get(f'http://gethorario:5000/listar/horario/?numHor={obj.numHor}')
            response.raise_for_status()
            data = response.json()

            if isinstance(data, list) and data:
                # Si la API devuelve un diccionario como {'fecHora': '2025-07-04'}
                if isinstance(data[0], dict) and 'fecHora' in data[0]:
                    return data[0]['fecHora']
                # Si la API devuelve directamente la fecha como un string
                elif isinstance(data[0], str):
                    return data[0]
            return "No encontrado"
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener fecHora para numHor {obj.numHor}: {e}")
            return "Error al cargar fecha"
        except Exception as e:
            print(f"Error inesperado al obtener fecHora: {e}")
            return "Error inesperado"

    def get_hora(self, obj):
        try:
            # Nueva API para el detalle de la hora específica
            response = requests.get(f'http://gethora:5000/listar/hora/?codHor={obj.codHor}')
            response.raise_for_status()
            data = response.json()

            if isinstance(data, list) and data:
                # Asumimos que la API devuelve un diccionario como {'nomMed': 'Roberto', 'especialidad': 'Cardiología'}
                if isinstance(data[0], dict):
                    return {
                        'horaIni': data[0].get('horaIni', 'No disponible'),
                        'especialidad': data[0].get('horaFin', 'No disponible') # Asume que el campo se llama 'especialidad'
                    }
            return {'hora': 'No encontrado', 'especialidad': 'No encontrado'}
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener detalle de hora para codHor {obj.codHor}: {e}")
            return "Error al cargar detalle de hora"
        except Exception as e:
            print(f"Error inesperado al obtener detalle de hora: {e}")
            return "Error inesperado"