from rest_framework import generics, status
from rest_framework.response import Response
from .models import Horario
from .serializers import HorarioSerializer

class HorarioCreateView(generics.CreateAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)