from django.db import models
from uuid import uuid4
#AbstractBaseUser te permite modificar todo por completo desde 0 con nuevas config
#AbstractUser Permite agregar nuevas columnas a la configuracion inicial, Solo para agregar 1 o 2
#PermissionsMixin Configurar como estara relacionada la nueva tabla con relacion a los permisos
#BaseUserManager Es el administrador sobre algunos comandos de la terminal como: cuando llamamos al createsuperuser este manejara este comportamiento
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class ManejadorUsuario(BaseUserManager):
    #Este sera el metodoq ue se llamara cuando en la terminal se quiera crear un nuevo usuario
    def create_superuser(self, nombre, correo, password):
        #Validamos si el correo no esta vacio

        if not correo or len(correo) == 0: 
            raise ValueError("El correo es obligatorio!")

        #normalize_email: Quita los espacios en blanco de los laterales, lo convierte todo a minusculas y borra los caracteles especiales como tildes u otros
        correoNormalizado = self.normalize_email(correo)

        #Con esto creamos la nueva instancia o registro del usuario
        nuevoUsuario = self.model(correo = correoNormalizado, nombre = nombre)
        #Este set_password se encarga de generar el hash para el password y guadarlo en la columna
        nuevoUsuario.set_password(password)

        #ahora modificamos los camposq ue usa el panel admin
        #is_superuser | is_staff
        nuevoUsuario.is_superuser = True
        nuevoUsuario.is_staff = True

        #Guardamos el registro en la bd
        nuevoUsuario.save()



class Especialidad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nombre = models.TextField(null=False)

    class Meta:
        db_table = 'especialidades'

#Vamos a cambiar la herencia de modelo y corriente al modelo encargado del auth_user
class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nombre = models.TextField()
    sexo = models.TextField()
    correo = models.TextField(unique=True)
    password = models.TextField()

    # Si aun queremos usar el panel administrativo tenemos que agregar estos atributos
    if_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    #Este atributo sirve para poder indicar cual es la columna para poder indenticar al usuario al momento de hacer logun ene l padel de administrativo
    #Este es aparte para el panel administrativo
    USERNAME_FIELD = 'correo' #Correo pq es unico

    #Sirve para que cuado se quiera crear un super user en la terminal se debe indicar que campos va solicitar
    #No se deben colocar los mismo atributos del username_field pq ya esta implicito y asi mismo el password SIEMPRE sera solicitado
    REQUIRED_FIELDS = ["nombre"]

    #Modificamos el comportamiento de nuestro auth_user y le asignamos la forma de creacion de un superuser en la terminal
    objects = ManejadorUsuario()

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
