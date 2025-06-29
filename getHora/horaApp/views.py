from rest_framework import generics
from .models import Hora
from .serializers import HoraSerializer

class HoraListView(generics.ListAPIView):
    serializer_class = HoraSerializer

    def get_queryset(self):
        queryset = Hora.objects.all()
        codHora = self.request.query_params.get('codHora', None)
        horaIni = self.request.query_params.get('horaIni', None)

        if codHora is not None:
            queryset = queryset.filter(codHora=codHora)
        if horaIni is not None:
            queryset = queryset.filter(horaIni=horaIni)

        return queryset