from django.db import models

# Create your models here.
class Funcionario(models.Model):
    cartao = models.DecimalField(null=False,
                                 blank=False,
                                 max_digits=14,
                                 decimal_places=0)
    nome = models.CharField(max_length=200,
                            null=False,
                            blank=False)
    empresa = models.ForeignKey(
        "Empresa", related_name='funcionarios', on_delete=models.CASCADE)


class Empresa(models.Model):
    nome = models.CharField(max_length=100,
                            null=False,
                            blank=False)


class Cesta(models.Model):
    nome = models.CharField(max_length=100,
                            null=False,
                            blank=False)
    quantidade = models.IntegerField(default=0,
                                     null=False,
                                     blank=False)


class FuncionarioCesta(models.Model):
    funcionario = models.ForeignKey(
        "Funcionario", on_delete=models.CASCADE)
    cesta = models.ForeignKey(
        "Cesta", on_delete=models.CASCADE)
    dataEntrega = models.DateField(auto_now_add=True)
