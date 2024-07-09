from django.urls import path, include
from .views import AreasFull,CargosFull,RolesFull, EmpleadosFull, MarcacionesFull,UsersFull

urlpatterns = [
    path('api/areas', AreasFull),
    path('api/areas/<id>', AreasFull),
    path('api/cargos', CargosFull),
    path('api/cargos/<id>', CargosFull),
    path('api/roles', RolesFull),
    path('api/roles/<id>', RolesFull),
    path('api/empleados', EmpleadosFull),
    path('api/empleados/<id>', EmpleadosFull),
    path('api/marcaciones', MarcacionesFull),
    path('api/marcaciones/<id>', MarcacionesFull),
    path('api/usuarios/', UsersFull),
    path('api/usuarios/<id>', UsersFull),
    

    
]