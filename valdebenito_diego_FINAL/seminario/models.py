from django.db import models

# Create your models here.

class Institucion(models.Model):
    nombre_institucion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_institucion

class Inscrito(models.Model):
    ESTADOS = [('RESERVADO', 'Reservado'),('COMPLETADA', 'Completada'),('ANULADA', 'Anulada'),('NO ASISTEN', 'No Asisten')]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    hora_inscripcion = models.TimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    observacion = models.TextField()

    def __str__(self):
        return self.nombre
