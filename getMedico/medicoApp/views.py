from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Medico

class MedicoListView(APIView):
    def get(self, request, especial, *args, **kwargs):
        queryset = Medico.objects.all()

        if not queryset:
            return Response(
                {"error": f"especial '{especial}' no válida."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if especial is not None:
            queryset = queryset.filter(codMed=especial)

        data_values = queryset.values_list('nomMed', flat=True)
        return Response(data_values, status=status.HTTP_200_OK)