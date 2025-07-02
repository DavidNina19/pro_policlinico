from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Horario

class HorarioListView(APIView):
    def get(self, request, ident, *args, **kwargs):
        queryset = Horario.objects.all()

        if not queryset:
            return Response(
                {"error": f"ident '{ident}' no válida."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if ident is not None:
            queryset = queryset.filter(numHor=ident)

        data_values = queryset.values_list('fecHora', flat=True)
        return Response(data_values, status=status.HTTP_200_OK)