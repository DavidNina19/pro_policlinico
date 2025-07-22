from django.db import models

class Analisis(models.Model):
    codTipo = models.AutoField(primary_key=True)
    tipoAnalisis = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.codTipo} ({self.tipoAnalisis})"

    class Meta:
        db_table = 'analisis'  # Mapea a la tabla 'analisis' en MySQL