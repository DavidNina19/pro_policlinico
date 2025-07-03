from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .models import Paciente

class RegistroPaciente(APIView):
    def post(self, request):
        data = request.data
        if Paciente.objects.filter(dni=data.get('dni')).exists():
            return Response({'error': 'DNI ya registrado'}, status=status.HTTP_400_BAD_REQUEST)

        paciente = Paciente.objects.create(
            dni=data['dni'],
            nombre=data['nombre'],
            apellido=data['apellido'],
            edad=data['edad'],
            email=data['email'],
            celular=data['celular'],
            password=make_password(data['password'])
        )
        return Response({'mensaje': 'Registro exitoso'}, status=status.HTTP_201_CREATED)