from django.db import models


class Pais(models.Model):
    codigo=models.CharField(max_length=3, primary_key=True)
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=1000)
    
class HDI(models.Model):
    pais=models.ForeignKey(Pais)
    hdi=models.CharField(max_length=10)
    
# Create your models here.
