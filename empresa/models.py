from django.db import models
from user.models import UsuarioChefe


class Empresa(models.Model):
    usuario = models.ForeignKey(UsuarioChefe, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=14)
    codigo_local = models.CharField(max_length=10)
