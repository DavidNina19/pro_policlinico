# app_name/serializers.py
from rest_framework import serializers
from .models import DetalleReceta # Asegúrate de importar el nuevo modelo
import requests
class DetalleRecetaSerializer(serializers.ModelSerializer):
    # Campos que vienen de microservicios externos
    #codReceDetalleReceta = serializers.SerializerMethodField()
    id_medi = serializers.SerializerMethodField()

    class Meta:
        model = DetalleReceta
        # Incluye todos los campos del modelo DetalleReceta y los campos obtenidos
        fields = ['codReceta', 'id_medi']

    def get_id_medi(self, obj):
        try:
            response = requests.get(f'http://getmedicamentos:5000/listar/medicamentos?id_medi={obj.id_medi}') # Usando codMed 
            response.raise_for_status() 
            data = response.json()
            
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and data:
                    return data[0]
            return "No encontrado"
        except Exception as e:
            return f"Error: {e}"

        