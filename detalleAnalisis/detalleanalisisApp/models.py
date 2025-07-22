from django.db import models

class DetalleAnalisis(models.Model):
    codAnalisis = models.AutoField(primary_key=True) # ID del Analisisrio, único para cada detalle de Analisis
    codTipo = models.IntegerField()            # ID del médico

    def __str__(self):
        return f"Detalle Analisis {self.codAnalisis} - tipoAnalisis {self.codTipo}"
    class Meta:
        db_table = 'detalleanalisis'