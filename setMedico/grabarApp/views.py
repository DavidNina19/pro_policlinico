from rest_framework import generics, status
from rest_framework.response import Response
from .models import Medico
from .serializers import MedicoSerializer

class MedicoCreateView(generics.CreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)