# app_name/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Medico
from .serializers import MedicoSerializer # Importa tu serializer

class MedicoListView(APIView):
    def get(self, request, *args, **kwargs):
        codMed = request.query_params.get('codMed')
        especial = request.query_params.get('especial')

        queryset = Medico.objects.filter(estado='A') 
        
        if codMed:
            queryset = queryset.filter(codMed=codMed)
        elif especial:
            queryset = queryset.filter(especial__iexact=especial)

        if not queryset.exists():
            return Response({"error": "No se encontraron médicos con los criterios proporcionados."},
                            status=status.HTTP_404_NOT_FOUND)

        # Serializa el queryset
        serializer = MedicoSerializer(queryset, many=True) # many=True si esperas una lista de objetos
        return Response(serializer.data, status=status.HTTP_200_OK)