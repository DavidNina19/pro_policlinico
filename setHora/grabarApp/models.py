from django.db import models

class Hora(models.Model):
    codHora = models.AutoField(primary_key=True)
    horaIni = models.TimeField()
    horaFin = models.TimeField()

    def __str__(self):
        return f"{self.horaIni} - {self.horaFin}"
    
    class Meta:
        db_table = 'hora'  # Usa la tabla existente 'Hora'