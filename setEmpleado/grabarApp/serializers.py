from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['codEmp', 'nomEmp', 'login', 'clave']  # Cambiado de pass a clave
        read_only_fields = ['codEmp']