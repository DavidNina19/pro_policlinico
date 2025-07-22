from rest_framework import serializers
from .models import Horario

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['numHor', 'fecHora', 'codEmp']
        #read_only_fields = ['codMed']  # codMed es autoincrementable