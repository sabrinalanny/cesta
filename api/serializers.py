from rest_framework import serializers
from api.models import Funcionario, Empresa, Cesta, FuncionarioCesta

class EmpresaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Empresa
    fields = ['nome']
    
class FuncionarioSerializer(serializers.ModelSerializer):
  #nomeEmpresa = serializers.ReadOnlyField(source='empresa.nome')
  empresas = EmpresaSerializer(read_only=True,many=True)
  class Meta:
    model = Funcionario
    fields = [
      'id',
      'cartao',
      'nome',
      'empresa',
      'empresas'
      #'nomeEmpresa'
    ]
    
class CestaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cesta
    fields = ['nome', 'quantidade']
    
class FuncionarioCestaSerializer(serializers.ModelSerializer):
  class Meta:
    model = FuncionarioCesta
    fields = ['funcionario', 'cesta', 'dataEntrega']