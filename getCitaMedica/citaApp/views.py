# clinica/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CitaMedica # Importa tu modelo CitaMedica
from .serializers import CitaMedicaSerializer # Importa el serializador

class getCitaMedica(APIView):

    def get(self, request):
        """
        Maneja las solicitudes GET para obtener una lista de todas las citas médicas.
        Serializa los objetos CitaMedica y los devuelve como respuesta JSON.
        """
        
        citas = CitaMedica.objects.all()
        serializer = CitaMedicaSerializer(citas, many=True) # many=True para serializar una lista de objetos
        return Response(serializer.data, status=status.HTTP_200_OK)

