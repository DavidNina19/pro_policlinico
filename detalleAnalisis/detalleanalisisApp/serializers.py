# app_name/serializers.py
from rest_framework import serializers
from .models import DetalleAnalisis # Asegúrate de importar el nuevo modelo
import requests
class DetalleAnalisisSerializer(serializers.ModelSerializer):
    # Campos que vienen de microservicios externos
    #codAnalisis = serializers.SerializerMethodField()
    codTipo = serializers.SerializerMethodField()

    class Meta:
        model = DetalleAnalisis
        # Incluye todos los campos del modelo DetalleAnalisis y los campos obtenidos
        fields = ['codAnalisis', 'codTipo']

    def get_codTipo(self, obj):
        try:
            response = requests.get(f'http://getanalisis:5000/listar/analisis?codTipo={obj.codTipo}') # Usando codMed 
            response.raise_for_status() 
            data = response.json()
            
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and data:
                    return data[0]
            return "No encontrado"
        except Exception as e:
            return f"Error: {e}"

        