from django.db import models

class DetalleMedico(models.Model):
    numHor = models.IntegerField()
    codMed = models.IntegerField()

    def __str__(self):
            return f"{self.numHor} {self.codMed}"

    class Meta:
        db_table = 'detallemedico'

# Create your models here.
