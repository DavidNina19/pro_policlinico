from rest_framework import generics, status
from rest_framework.response import Response
from .models import Hora
from .serializers import HoraSerializer

class HoraCreateView(generics.CreateAPIView):
    queryset = Hora.objects.all()
    serializer_class = HoraSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)