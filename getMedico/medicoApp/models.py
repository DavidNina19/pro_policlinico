from django.db import models

class Medico(models.Model):
    codMed = models.AutoField(primary_key=True)
    nomMed = models.CharField(max_length=100)
    especial = models.CharField(max_length=100)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nomMed} ({self.especial})"

    class Meta:
        db_table = 'medico'  # Mapea a la tabla 'medico' en MySQL