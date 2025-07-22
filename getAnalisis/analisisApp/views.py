# app_name/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Analisis
from .serializers import AnalisisSerializer # Importa tu serializer

class AnalisisListView(APIView):
    def get(self, request, *args, **kwargs):
        codTipo = request.query_params.get('codTipo')
        tipoAnalisis = request.query_params.get('tipoAnalisis')

        queryset = Analisis.objects.all() 
        
        if codTipo:
            queryset = queryset.filter(codTipo=codTipo)
        elif tipoAnalisis:
            queryset = queryset.filter(tipoAnalisis__iexact=tipoAnalisis)

        if not queryset.exists():
            return Response({"error": "No se encontraron médicos con los criterios proporcionados."},
                            status=status.HTTP_404_NOT_FOUND)

        # Serializa el queryset
        serializer = AnalisisSerializer(queryset, many=True) # many=True si esperas una lista de objetos
        return Response(serializer.data, status=status.HTTP_200_OK)