from django.db import models

class AtencionMedica(models.Model):
    codAte = models.AutoField(primary_key=True)
    codCita = models.IntegerField()
    id_receta = models.IntegerField()
    codAnalisis = models.IntegerField()
    diagnostico = models.CharField(max_length=255)
    tratamiento = models.CharField(max_length=150)
    t_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f"{self.codAte} {self.codCita} {self.id_receta} {self.codAnalisis} {self.diagnostico} {self.tratamiento} {self.t_stamp}"

    class Meta:
        db_table = 'atencionmedica'

# Create your models here.
