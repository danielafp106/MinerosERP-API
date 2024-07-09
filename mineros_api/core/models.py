from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

class RolesUsuarios(models.Model):
    id_rol_usuario = models.AutoField(primary_key=True)
    rol_usuario = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'roles_usuarios'
        verbose_name = "roles_usuarios"
        verbose_name_plural = "roles_usuarios"
    
    def __str__(self):
        return self.rol_usuario

class User(AbstractUser):
    id_rol_usuario = models.ForeignKey(RolesUsuarios, models.DO_NOTHING, db_column='id_rol_usuario', default=1)

    def __str__(self):
        return self.username

class Areas(models.Model):
    id_area = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'areas'
        verbose_name = "areas"
        verbose_name_plural = "areas"
    
    def __str__(self):
        return self.nombre_area


class CargosEmpleados(models.Model):
    id_cargos_empleado = models.AutoField(primary_key=True)
    cargos_empleado = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'cargos_empleados'
        verbose_name = "cargos_empleados"
        verbose_name_plural = "cargos_empleados"
    
    def __str__(self):
        return self.cargos_empleado


class Empleados(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombres_empleado = models.CharField(max_length=100)
    apellidos_empleado = models.CharField(max_length=100)
    direccion_empleado = models.CharField(max_length=250)
    dui_empleado = models.CharField(max_length=9)
    fecha_nacimiento_empleado = models.DateField()
    telefono_empleado = models.CharField(max_length=9)
    numero_isss_empleado = models.CharField(max_length=10)
    numero_afp_empleado = models.CharField(max_length=12)
    sueldo_empleado = models.FloatField()
    id_cargo_empleado = models.ForeignKey(CargosEmpleados, models.DO_NOTHING, db_column='id_cargo_empleado')
    id_area = models.ForeignKey(Areas, models.DO_NOTHING, db_column='id_area')
    id_usuario = models.ForeignKey(User, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = True
        db_table = 'empleados'
        verbose_name = "empleados"
        verbose_name_plural = "empleados"

    def __str__(self):
        return self.apellidos_empleado


class MarcacionEmpleados(models.Model):
    id_marcacion = models.AutoField(primary_key=True)
    fecha_marcacion = models.DateField()
    hora_entrada = models.CharField(max_length=25)
    hora_salida = models.CharField(max_length=25)
    tipo_marcacion = models.CharField(max_length=25)
    id_empleado = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='id_empleado')

    class Meta:
        managed = True
        db_table = 'marcacion_empleados'
        verbose_name = "marcacion_empleados"
        verbose_name_plural = "marcacion_empleados"
    





