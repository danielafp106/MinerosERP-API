from django.shortcuts import render
from .serializers import AreasSrlzr, CargosSrlzr, UserSrlzr,RolesSrlzr, EmpleadosSrlzr, MarcacionesSrlzr
from .models import Areas, CargosEmpleados, User,RolesUsuarios, Empleados, MarcacionEmpleados
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
import json
from django.http import HttpResponse,JsonResponse
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

@api_view(['GET', 'DELETE', 'POST', 'PUT'])
@permission_classes([AllowAny])
def AreasFull(request, id=None):
    try:
        if id is None:
            areas = Areas.objects.all()
            srlzr = AreasSrlzr(areas, many = True)
        else:
            areas = Areas.objects.get(pk = id)
            srlzr = AreasSrlzr(areas)
        
        if request.method == 'GET':           
            return JsonResponse(srlzr.data, safe=False)

        elif request.method == 'POST':
            data=JSONParser().parse(request)
            srlzr = AreasSrlzr(data=data)
            if srlzr.is_valid():
                srlzr.save()
                return JsonResponse(srlzr.data,status=status.HTTP_201_CREATED)
            return JsonResponse(srlzr.errors,status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            areas.delete()
            return JsonResponse({'Message': 'Área eliminada con exito'}, status=status.HTTP_204_NO_CONTENT)
        
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            srlzr = AreasSrlzr(areas, data=data)
            if srlzr.is_valid():
                srlzr.save()
                return JsonResponse(srlzr.data)
            return JsonResponse(srlzr.errors, status=status.HTTP_400_BAD_REQUEST)

    except Areas.DoesNotExist:
        return JsonResponse({'message': 'El área no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'DELETE', 'POST', 'PUT'])
@permission_classes([AllowAny])
def CargosFull(request, id=None):
    try:
        if id is None:
            cargos = CargosEmpleados.objects.all()
            srlzr = CargosSrlzr(cargos, many = True)
        else:
            cargos = CargosEmpleados.objects.get(pk = id)
            srlzr = CargosSrlzr(cargos)
        
        if request.method == 'GET':           
            return JsonResponse(srlzr.data, safe=False)

        elif request.method == 'POST':
            data=JSONParser().parse(request)
            srlzr = CargosSrlzr(data=data)
            if srlzr.is_valid():
                srlzr.save()
                return JsonResponse(srlzr.data,status=status.HTTP_201_CREATED)
            return JsonResponse(srlzr.errors,status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            cargos.delete()
            return JsonResponse({'Message': 'Cargo eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)
        
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            srlzr = CargosSrlzr(cargos, data=data)
            if srlzr.is_valid():
                srlzr.save()
                return JsonResponse(srlzr.data)
            return JsonResponse(srlzr.errors, status=status.HTTP_400_BAD_REQUEST)

    except CargosEmpleados.DoesNotExist:
        return JsonResponse({'message': 'El cargo no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'DELETE', 'POST', 'PUT'])
@permission_classes([AllowAny])
def RolesFull(request, id=None):
    try:
        if id is None:
            roles = RolesUsuarios.objects.all()
            srlzr = RolesSrlzr(roles, many = True)
        else:
            roles = RolesUsuarios.objects.get(pk = id)
            srlzr = RolesSrlzr(roles)
        
        if request.method == 'GET':           
            return JsonResponse(srlzr.data, safe=False)

        elif request.method == 'POST':
            data=JSONParser().parse(request)
            srlzr = RolesSrlzr(data=data)
            if srlzr.is_valid():
                srlzr.save()
                return JsonResponse(srlzr.data,status=status.HTTP_201_CREATED)
            return JsonResponse(srlzr.errors,status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            roles.delete()
            return JsonResponse({'Message': 'Rol eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)
        
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            srlzr = RolesSrlzr(roles, data=data)
            if srlzr.is_valid():
                srlzr.save()
                return JsonResponse(srlzr.data)
            return JsonResponse(srlzr.errors, status=status.HTTP_400_BAD_REQUEST)

    except RolesUsuarios.DoesNotExist:
        return JsonResponse({'message': 'El rol no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'DELETE', 'POST', 'PUT'])
@permission_classes([AllowAny])
def EmpleadosFull(request, id=None):
    try:
        if id is None:
            empleado = Empleados.objects.all()
            srlzr = EmpleadosSrlzr(empleado, many = True)
        else:
            empleado = Empleados.objects.get(pk = id)
            srlzr = EmpleadosSrlzr(empleado)
        
        if request.method == 'GET':           
            return JsonResponse(srlzr.data, safe=False)

        elif request.method == 'POST':
            data=JSONParser().parse(request)
            srlzr = EmpleadosSrlzr(data=data)
            if srlzr.is_valid():
                srlzr.save()
                return JsonResponse(srlzr.data,status=status.HTTP_201_CREATED)
            return JsonResponse(srlzr.errors,status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            empleado.delete()
            return JsonResponse({'Message': 'Empleado eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)
        
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            srlzr = EmpleadosSrlzr(empleado, data=data)
            if srlzr.is_valid():
                srlzr.save()
                return JsonResponse(srlzr.data)
            return JsonResponse(srlzr.errors, status=status.HTTP_400_BAD_REQUEST)

    except Empleados.DoesNotExist:
        return JsonResponse({'message': 'El empleado no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'DELETE', 'POST', 'PUT'])
@permission_classes([AllowAny])
def MarcacionesFull(request, id=None):
    try:
        if id is None:
            marcacion = MarcacionEmpleados.objects.all()
            srlzr = MarcacionesSrlzr(marcacion, many = True)
        else:
            marcacion = MarcacionEmpleados.objects.get(pk = id)
            srlzr = MarcacionesSrlzr(marcacion)
        
        if request.method == 'GET':           
            return JsonResponse(srlzr.data, safe=False)

        elif request.method == 'POST':
            data=JSONParser().parse(request)
            srlzr = MarcacionesSrlzr(data=data)
            if srlzr.is_valid():
                srlzr.save()
                return JsonResponse(srlzr.data,status=status.HTTP_201_CREATED)
            return JsonResponse(srlzr.errors,status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            marcacion.delete()
            return JsonResponse({'Message': 'Registro eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)
        
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            srlzr = MarcacionesSrlzr(marcacion, data=data)
            if srlzr.is_valid():
                srlzr.save()
                return JsonResponse(srlzr.data)
            return JsonResponse(srlzr.errors, status=status.HTTP_400_BAD_REQUEST)

    except MarcacionEmpleados.DoesNotExist:
        return JsonResponse({'message': 'Ese registro no existe'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([AllowAny])
def UsersFull(request, id=None):
    try:
        User = get_user_model()
        if id is None:
            usuario = User.objects.all()
            srlzr = UserSrlzr(usuario, many = True)
        else:
            usuario = User.objects.get(pk = id)
            srlzr = UserSrlzr(usuario)
        
        if request.method == 'GET':           
            return JsonResponse(srlzr.data, safe=False)
            
    except User.DoesNotExist:
        return JsonResponse({'message': 'El usuario no existe'}, status=status.HTTP_404_NOT_FOUND)