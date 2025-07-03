from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .models import Paciente

class LoginPaciente(APIView):
    def get(self, request):
        dni = request.query_params.get('dni')
        password = request.query_params.get('password')

        try:
            paciente = Paciente.objects.get(dni=dni, estado='A')
            if check_password(password, paciente.password):
                return Response({'mensaje': 'Login exitoso'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        except Paciente.DoesNotExist:
            return Response({'error': 'Usuario no encontrado o inactivo'}, status=status.HTTP_404_NOT_FOUND)
