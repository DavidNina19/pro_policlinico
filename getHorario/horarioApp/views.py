from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Horario
from .serializers import HorarioSerializer # Asegúrate de que este serializer exista y esté bien definido

class HorarioListView(APIView):
    def get(self, request, *args, **kwargs):
        # Obtener los parámetros de consulta
        fecHora = request.query_params.get('fecHora') # Para filtrar por fecha
        numHor = request.query_params.get('numHor')   # Para filtrar por número de horario

        queryset = Horario.objects.all()

        # Aplicar filtros si los parámetros están presentes
        if fecHora:
            queryset = queryset.filter(fecHora=fecHora)
        
        if numHor:
            queryset = queryset.filter(numHor=numHor)

        # Si no se encontraron resultados después de aplicar los filtros
        if not queryset.exists():
            # Mensaje de error más específico
            error_message = "No se encontraron horarios con los criterios proporcionados."
            if fecHora:
                error_message += f" (Fecha: {fecHora})"
            if numHor:
                error_message += f" (NumHor: {numHor})"
            
            return Response(
                {"error": error_message},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Serializa los resultados
        serializer = HorarioSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)