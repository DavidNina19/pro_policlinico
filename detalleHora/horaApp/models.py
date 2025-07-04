from django.db import models

class DetalleHora(models.Model):
    numHor = models.IntegerField() # ID del horario, único para cada detalle de hora
    codMed = models.IntegerField()            # ID del médico
    codHor = models.IntegerField()            # ID de la hora específica
    consul = models.CharField(max_length=100) # Campo 'consul'
    estado = models.CharField(max_length=1, default='A') # Campo 'estado'

    def __str__(self):
        return f"Detalle Hora {self.numHor} - Médico {self.codMed}"
    class Meta:
        db_table = 'detallehora'