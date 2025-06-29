from rest_framework import generics
from .models import Empleado
from .serializers import EmpleadoSerializer

class EmpleadoListView(generics.ListAPIView):
    serializer_class = EmpleadoSerializer

    def get_queryset(self):
        queryset = Empleado.objects.all()
        codEmp = self.request.query_params.get('codEmp', None)

        if codEmp is not None:
            queryset = queryset.filter(codEmp=codEmp)
    
        return queryset