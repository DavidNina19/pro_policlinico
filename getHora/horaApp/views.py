from rest_framework import generics
from .models import Hora
from .serializers import HoraSerializer

class HoraListView(generics.ListAPIView):
    serializer_class = HoraSerializer

    def get_queryset(self):
        queryset = Hora.objects.all()
        codHor = self.request.query_params.get('codHor', None)
        horaIni = self.request.query_params.get('horaIni', None)

        if codHor is not None:
            queryset = queryset.filter(codHor=codHor)
        if horaIni is not None:
            queryset = queryset.filter(horaIni=horaIni)

        return queryset