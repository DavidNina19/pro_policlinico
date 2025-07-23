from django.db import models

class DetalleReceta(models.Model):
    id_receta = models.AutoField(primary_key=True)
    codReceta = models.IntegerField() # ID del Recetario, único para cada detalle de Receta
    id_medi = models.IntegerField()            # ID del médico

    def __str__(self):
        return f"Detalle Receta {self.id_receta} - tipoReceta {self.id_medi} - codReceta {self.codReceta}"
    class Meta:
        db_table = 'detallereceta'