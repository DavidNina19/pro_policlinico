from django.db import models

# Create your models here.
class CitaMedica(models.Model):
    codCita = models.AutoField(primary_key=True)
    numHor = models.CharField(max_length=10)
    codMed = models.CharField(max_length=10)
    codHor = models.CharField(max_length=10)
    codPago = models.CharField(max_length=10)
    dni = models.CharField(max_length=10, default='12345678')  # DNI del paciente
    consultorio = models.CharField(max_length=5) 
    estado = models.CharField(max_length=1, default='A')  # A: Activa, C: Cancelada, R: Realizada
    t_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cita de {self.paciente} con {self.doctor} el {self.fecha} a las {self.hora}"
    
    class Meta:
        db_table = 'cita_medica'