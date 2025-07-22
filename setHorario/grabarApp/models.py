from django.db import models

class Horario(models.Model):
    numHor = models.AutoField(primary_key=True)
    fecHora = models.DateField()
    codEmp = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.fecHora} ({self.codEmp})"

    class Meta:
        db_table = 'horario'  # Mapea a la tabla 'horario' en MySQL