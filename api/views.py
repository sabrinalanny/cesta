from django.shortcuts import render

from api.serializers import FuncionarioSerializer, EmpresaSerializer, CestaSerializer, FuncionarioCestaSerializer
from rest_framework import viewsets, permissions
from api.models import Funcionario, Empresa, Cesta, FuncionarioCesta


class FuncionarioViewSet(viewsets.ModelViewSet):
  queryset = Funcionario.objects.all()
  serializer_class = FuncionarioSerializer
  permission_classes = [permissions.IsAuthenticated]
  
class EmpresaViewSet(viewsets.ModelViewSet):
  queryset = Empresa.objects.all()
  serializer_class = EmpresaSerializer
  permission_classes = [permissions.IsAuthenticated]
  
class CestaViewSet(viewsets.ModelViewSet):
  queryset = Cesta.objects.all()
  serializer_class = CestaSerializer
  permission_classes = [permissions.IsAuthenticated]  
  
class FuncionarioCestaViewSet(viewsets.ModelViewSet):
  queryset = FuncionarioCesta.objects.all()
  serializer_class = FuncionarioCestaSerializer
  permission_classes = [permissions.IsAuthenticated]