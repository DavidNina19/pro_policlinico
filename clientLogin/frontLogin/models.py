from django.db import models

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()
    celular = models.CharField(max_length=20)
    password = models.TextField()
    estado = models.CharField(max_length=1, default='A')  # Activo/Inactivo
    cargo = models.CharField(max_length=20, default='paciente')  # paciente / admin

    class Meta:
        db_table = 'paciente'

    def __str__(self):
        return f"{self.dni} - {self.nombre}"
