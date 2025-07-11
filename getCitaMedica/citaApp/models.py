from django.db import models

# Create your models here.
class CitaMedica(models.Model):
    codCita = models.AutoField(primary_key=True)
    numHor = models.CharField(max_length=10)
    codMed = models.CharField(max_length=10)
    codHor = models.CharField(max_length=10)
    #codPago = models.CharField(max_length=10)
    dni = models.CharField(max_length=10)  # DNI del paciente
    consultorio = models.CharField(max_length=5) 
    estado = models.CharField(max_length=1, default='P')  # A: Activa, C: Cancelada, P: Pendiente
    t_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cita de {self.codCita} con {self.numHor} el {self.codMed} a las {self.codPago}"
    
    class Meta:
        db_table = 'cita_medica'