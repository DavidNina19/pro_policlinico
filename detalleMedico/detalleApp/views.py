from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DetalleMedico
from .serializers import DetalleMedicoSerializer

# Crear DetalleMedico (POST)
class DetalleMedicoCreateView(APIView):
    def post(self, request):
        serializer = DetalleMedicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Listar todos los registros (GET)
class DetalleMedicoListView(APIView):
    def get(self    , request):
        detalles = DetalleMedico.objects.all()
        serializer = DetalleMedicoSerializer(detalles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
