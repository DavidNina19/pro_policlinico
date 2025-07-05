# app_name/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DetalleHora # Importa el nuevo modelo
from .serializers import DetalleHoraSerializer # Importa el nuevo serializer

# Crear DetalleHora (POST)
class DetalleHoraCreateView(APIView):
    def post(self, request):
        serializer = DetalleHoraSerializer(data=request.data)
        if serializer.is_valid():
            # Los campos nomMed, fecHora y horarioDetalle son SerializerMethodField
            # y no deben ser guardados directamente en el modelo DetalleHora.
            # Asegúrate de que los datos enviados en el POST no incluyan estos campos
            # o que el serializer los ignore en la escritura.
            # Al usar ModelSerializer, por defecto, los SerializerMethodField son read_only.
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Listar todos los registros o filtrar por campos locales (GET)
class DetalleHoraListView(APIView):
    def get(self, request, *args, **kwargs):
        # Puedes añadir parámetros de consulta para filtrar los campos locales si es necesario
        numHor_param = request.query_params.get('numHor')
        codMed_param = request.query_params.get('codMed')
        estado_param = request.query_params.get('estado')

        queryset = DetalleHora.objects.all()

        if numHor_param:
            queryset = queryset.filter(numHor=numHor_param)
        if codMed_param:
            queryset = queryset.filter(codMed=codMed_param)
        if estado_param:
            queryset = queryset.filter(estado__iexact=estado_param) # Uso iexact para ignorar mayúsculas/minúsculas en el estado

        if not queryset.exists():
            return Response(
                {"error": "No se encontraron detalles de hora con los criterios proporcionados."},
                status=status.HTTP_404_NOT_FOUND
            )
            
        serializer = DetalleHoraSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)