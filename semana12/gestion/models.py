from django.db import models
from uuid import uuid4

# Create your models here.

class Especialidad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nombre = models.TextField(null=False)

    class Meta:
        db_table = 'especialidades'

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nombre = models.TextField()
    sexo = models.TextField()
    correo = models.TextField(unique=True)
    password = models.TextField()

    class Meta:
            db_table = 'usuarios'

class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    colegiatura = models.TextField()
    usuario = models.ForeignKey(to=Usuario, on_delete=models.PROTECT, db_column='usuario_id')

    class Meta:
        db_table = 'doctores'

class Paciente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    telefono = models.TextField(null=True)
    peso = models.FloatField(null=True)
    estatura = models.FloatField(null=True)
    usuario = models.ForeignKey(to=Usuario, on_delete=models.PROTECT, db_column='usuario_id')

    class Meta:
        db_table = 'pacientes'

class EspecialidadDoctor(models.Model):
    #Se usa esto cuando tenemos relacion de muchos a muchos para poder especificar llave primaria compuesta
    #Siemre debe tener el atributo llamado pk 
    pk = models.CompositePrimaryKey("doctor_id", "especialidad_id")
    doctor = models.ForeignKey(to=Doctor, on_delete=models.PROTECT, db_column='doctor_id')
    especialidad = models.ForeignKey(to=Especialidad, on_delete=models.PROTECT, db_column='especialidad_id')

    class Meta:
        db_table = 'especialidades_doctores'

ESTADO_CITAS = {
    "CONFIRMADO": "CONFIRMADO",
    "CANCELADO": "CANCELADO",
    "AGENDADO": "AGENDADO"
}

class Cita(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    fecha = models.DateField()
    horaInicio = models.TextField(db_column='hora_inicio')
    horaFin = models.TextField(db_column='hora_fin')
    estado = models.TextField(choices=ESTADO_CITAS, default=ESTADO_CITAS['AGENDADO'])
    observacion = models.TextField(null=True)
    consultorio = models.TextField(null=True)
    doctor = models.ForeignKey(to=Doctor, on_delete=models.PROTECT, db_column='doctor_id')
    paciente = models.ForeignKey(to=Paciente, on_delete=models.PROTECT, db_column='paciente_id')

    class Meta:
        db_table = 'citas'
