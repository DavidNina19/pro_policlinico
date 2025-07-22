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
    def get(self, request):
        detalles = DetalleAnalisis.objects.all()
        serializer = DetalleAnalisisSerializer(detalles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
