from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DetalleAnalisis
from .serializers import DetalleAnalisisSerializer

# Crear DetalleAnalisis (POST)
#class DetalleAnalisisCreateView(APIView):
#    def post(self, request):
#        serializer = DetalleAnalisisSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Listar todos los registros (GET)
class DetalleAnalisisListView(APIView):
    def get(self, request, *args, **kwargs):
        # Puedes añadir parámetros de consulta para filtrar los campos locales si es necesario
        codAnalisis_param = request.query_params.get('codAnalisis')
        codTipo = request.query_params.get('codTipo')

        queryset = DetalleAnalisis.objects.all()

        if codAnalisis_param:
            queryset = queryset.filter(codAnalisis=codAnalisis_param)
        if codTipo:
            queryset = queryset.filter(codTipo=codTipo)

        if not queryset.exists():
            return Response(
                {"error": "No se encontraron detalles de hora con los criterios proporcionados."},
                status=status.HTTP_404_NOT_FOUND
            )
            
        serializer = DetalleAnalisisSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
