from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AtencionMedica
from .serializers import AtencionMedicaSerializer

# Crear AtencionMedica (POST)
class AtencionMedicaCreateView(APIView):
    def post(self, request):
        serializer = AtencionMedicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Listar todos los registros (GET)
class AtencionMedicaListView(APIView):
    def get(self, request):
        detalles = AtencionMedica.objects.all()
        serializer = AtencionMedicaSerializer(detalles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
