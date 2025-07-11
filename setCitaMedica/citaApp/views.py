from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# No necesitamos make_password/check_password ya que CitaMedica no maneja contraseñas
# from django.contrib.auth.hashers import make_password, check_password 
from .models import CitaMedica # Importa tu modelo CitaMedica

class RegistroCitaMedica(APIView):
    """
    Vista para registrar nuevas citas médicas.
    Permite crear un nuevo registro de CitaMedica en la base de datos.
    """
    def post(self, request):
        data = request.data

        # Validar que los campos obligatorios estén presentes en la solicitud
        required_fields = ['numHor', 'codMed', 'codHor', 'consultorio', 'dni']
        for field in required_fields:
            if field not in data:
                return Response(
                    {'error': f'El campo "{field}" es obligatorio.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        try:
            # Crear la nueva instancia de CitaMedica
            # El campo 'codCita' es AutoField y se genera automáticamente.
            # El campo 't_stamp' es DateTimeField(auto_now_add=True) y se llena automáticamente.
            cita_medica = CitaMedica.objects.create(
                numHor=data['numHor'],
                codMed=data['codMed'],
                codHor=data['codHor'],
                consultorio=data['consultorio'],
                dni = data['dni'],
                # 'estado' es opcional, si no se proporciona, usa el valor por defecto 'A'
                estado=data.get('estado', 'P') 
            )
            # Retornar una respuesta de éxito con el ID de la cita creada
            return Response(
                {'mensaje': 'Cita médica registrada exitosamente', 'codCita': cita_medica.codCita},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            # Capturar cualquier otro error que pueda ocurrir durante la creación
            return Response(
                {'error': f'Error al registrar la cita médica: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )