from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Areas, CargosEmpleados, User, Empleados, MarcacionEmpleados, RolesUsuarios

class AreasSrlzr(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = '__all__'

class CargosSrlzr(serializers.ModelSerializer):
    class Meta:
        model = CargosEmpleados
        fields = '__all__'

class UserSrlzr(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'id','username','first_name','last_name','email','id_rol_usuario')

class RolesSrlzr(serializers.ModelSerializer):
    class Meta:
        model = RolesUsuarios
        fields = '__all__'

class EmpleadosSrlzr(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'

class MarcacionesSrlzr(serializers.ModelSerializer):
    class Meta:
        model = MarcacionEmpleados
        fields = '__all__'


        