from django.db import models

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.CharField(max_length=3)
    email = models.EmailField()
    celular = models.CharField(max_length=20)
    password = models.TextField()
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        db_table = 'paciente'

    def __str__(self):
        return f"{self.dni} - {self.nombre}"
