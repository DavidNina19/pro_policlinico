# app_name/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Medicamentos
from .serializers import MedicamentosSerializer # Importa tu serializer

class MedicamentosListView(APIView):
    def get(self, request, *args, **kwargs):
        id_medi = request.query_params.get('id_medi')
        nombre = request.query_params.get('nombre')

        queryset = Medicamentos.objects.all()
        
        if id_medi:
            queryset = queryset.filter(id_medi=id_medi)
        elif nombre:
            queryset = queryset.filter(nombre__iexact=nombre)

        if not queryset.exists():
            return Response({"error": "No se encontraron médicos con los criterios proporcionados."},
                            status=status.HTTP_404_NOT_FOUND)

        # Serializa el queryset
        serializer = MedicamentosSerializer(queryset, many=True) # many=True si esperas una lista de objetos
        return Response(serializer.data, status=status.HTTP_200_OK)