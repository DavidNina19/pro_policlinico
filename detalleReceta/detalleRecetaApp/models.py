from django.db import models

class DetalleReceta(models.Model):
    codReceta = models.AutoField(primary_key=True) # ID del Recetario, único para cada detalle de Receta
    id_medi = models.IntegerField()            # ID del médico

    def __str__(self):
        return f"Detalle Receta {self.codReceta} - tipoReceta {self.id_medi}"
    class Meta:
        db_table = 'detallereceta'