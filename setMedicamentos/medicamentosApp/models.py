from django.db import models

class Medicamentos(models.Model):
    id_medi = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    #cant = models.CharField(max_length=10)
    fec_ven = models.DateField()
    t_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id_medi} - {self.nombre} (Vence: {self.fec_ven})"

    class Meta:
        db_table = 'medicamentos'  # Mapea a la tabla 'medicamentos' en MySQL