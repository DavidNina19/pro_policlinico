from django.db import models

class Empleado(models.Model):
    codEmp = models.AutoField(primary_key=True)
    nomEmp = models.CharField(max_length=100)
    login = models.CharField(max_length=50)
    clave = models.CharField(max_length=100)  # Cambiado de pass_field a clave

    def __str__(self):
        return self.nomEmp

    class Meta:
        db_table = 'empleado'  # Mapea a la tabla 'empleado' en MySQL