from rest_framework import serializers
from .models import AtencionMedica

class AtencionMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtencionMedica
        fields = ['codAte', 'codCita', 'id_receta', 'codAnalisis', 'diagnostico', 'tratamiento', 't_stamp']
        read_only_fields = ['codAte']  # codMed es autoincrementable