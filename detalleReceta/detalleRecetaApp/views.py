from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DetalleReceta
from .serializers import DetalleRecetaSerializer

# Crear DetalleReceta (POST)
#class DetalleRecetaCreateView(APIView):
#    def post(self, request):
#        serializer = DetalleRecetaSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Listar todos los registros (GET)
class DetalleRecetaListView(APIView):
    def get(self, request):
        detalles = DetalleReceta.objects.all()
        serializer = DetalleRecetaSerializer(detalles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
