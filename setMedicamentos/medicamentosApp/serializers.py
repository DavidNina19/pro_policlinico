from rest_framework import serializers
from .models import Medicamentos

class MedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamentos
        fields = ['id_medi', 'fec_ven', 'nombre', 't_stamp']
        read_only_fields = ['id_medi']  # codMed es autoincrementable