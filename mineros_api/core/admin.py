from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Areas, CargosEmpleados, Empleados, MarcacionEmpleados, RolesUsuarios,User

admin.site.register(User,UserAdmin)
admin.site.register([Areas, CargosEmpleados, Empleados, MarcacionEmpleados, RolesUsuarios])
