# clinica/serializers.py

from rest_framework import serializers
from .models import CitaMedica
import requests # Necesario para hacer las llamadas HTTP a los microservicios

class CitaMedicaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo CitaMedica.
    Enriquece los datos de CitaMedica con información de microservicios externos
    para médico, fecha de horario y hora de inicio/fin.
    """
    # Campos que se obtendrán de microservicios externos
    # nomMed representa el detalle del médico asociado a codMed
    nomMed = serializers.SerializerMethodField()
    # fecHora representa la fecha del horario asociado a numHor
    fecHora = serializers.SerializerMethodField()
    # hora representa el detalle de la hora (inicio/fin) asociado a codHor
    hora = serializers.SerializerMethodField() 

    class Meta:
        model = CitaMedica
        # Incluye todos los campos del modelo CitaMedica y los campos enriquecidos.
        fields = ['codCita', 'numHor', 'codMed', 'codHor', 'dni', 'consultorio', 'estado', 't_stamp', 'nomMed', 'fecHora', 'hora']
        # 'codCita' y 't_stamp' son de solo lectura porque se generan automáticamente.
        # Los campos enriquecidos también son de solo lectura, no se esperan en la entrada.
        read_only_fields = ('codCita', 't_stamp', 'nomMed', 'fecHora', 'hora',)

    def get_nomMed(self, obj):
        """
        Obtiene el nombre y especialidad del médico desde el microservicio 'getmedico'.
        Utiliza obj.codMed para la consulta.
        """
        try:
            # Construye la URL para consultar el médico por su código
            # Nota: La URL proporcionada era '?nomMed={obj.codMed}/', pero si codMed es el ID,
            # es más común que el parámetro sea 'codMed'. Ajusta si 'nomMed' es correcto para el ID.
            response = requests.get(f'http://getmedico:5000/listar/medico/?codMed={obj.codMed}')
            response.raise_for_status() # Lanza una excepción para códigos de estado HTTP de error (4xx o 5xx)
            data = response.json()
            
            if isinstance(data, list) and data and isinstance(data[0], dict):
                # Extrae 'nomMed' y 'especial' del primer diccionario en la lista
                return {
                    'nomMed': data[0].get('nomMed', 'No disponible'),
                    'especial': data[0].get('especial', 'No disponible') 
                }
            return {'nomMed': 'No encontrado', 'especial': 'No encontrado'}
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener nomMed y especialidad para codMed {obj.codMed}: {e}")
            return {'nomMed': 'Error al cargar', 'especial': 'Error al cargar'}
        except Exception as e:
            print(f"Error inesperado al obtener nomMed y especialidad: {e}")
            return {'nomMed': 'Error inesperado', 'especial': 'Error inesperado'}

    def get_fecHora(self, obj):
        """
        Obtiene la fecha del horario desde el microservicio 'gethorario'.
        Utiliza obj.numHor para la consulta.
        """
        try:
            # Construye la URL para consultar el horario por su código numHor
            response = requests.get(f'http://gethorario:5000/listar/horario/?numHor={obj.numHor}')
            response.raise_for_status()
            data = response.json()

            if isinstance(data, list) and data and isinstance(data[0], dict) and 'fecHora' in data[0]:
                # Extrae 'fecHora' del primer diccionario en la lista
                return data[0]['fecHora']
            return "No encontrado"
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener fecHora para numHor {obj.numHor}: {e}")
            return "Error al cargar fecha"
        except Exception as e:
            print(f"Error inesperado al obtener fecHora: {e}")
            return "Error inesperado"

    def get_hora(self, obj):
        """
        Obtiene el detalle de la hora (horaIni, horaFin) desde el microservicio 'gethora'.
        Utiliza obj.codHor para la consulta.
        """
        try:
            # Construye la URL para consultar la hora por su codHor
            response = requests.get(f'http://gethora:5000/listar/hora/?codHor={obj.codHor}')
            response.raise_for_status()
            data = response.json()

            if isinstance(data, list) and data and isinstance(data[0], dict):
                # Extrae 'horaIni' y 'horaFin' del primer diccionario en la lista
                return {
                    'horaIni': data[0].get('horaIni', 'No disponible'),
                    'horaFin': data[0].get('horaFin', 'No disponible') 
                }
            return {'horaIni': 'No encontrado', 'horaFin': 'No encontrado'}
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener detalle de hora para codHor {obj.codHor}: {e}")
            return {'horaIni': 'Error al cargar', 'horaFin': 'Error al cargar'}
        except Exception as e:
            print(f"Error inesperado al obtener detalle de hora: {e}")
            return {'horaIni': 'Error inesperado', 'horaFin': 'Error inesperado'}
