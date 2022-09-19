from django.db import models

# Create your models here.
class Tabla_23_0(models.Model):
    id_job = models.CharField(max_length=30)
    job = models.CharField(max_length=30)
    carpeta = models.CharField(max_length=30)
    proceso = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    com = models.CharField(max_length=30)
    secuencia = models.CharField(max_length=30)
    hora = models.CharField(max_length=30)
    
class Tabla_0_1(models.Model):
    id_job = models.CharField(max_length=30)
    job = models.CharField(max_length=30)
    carpeta = models.CharField(max_length=30)
    proceso = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    com = models.CharField(max_length=30)
    secuencia = models.CharField(max_length=30)
    hora = models.CharField(max_length=30)

class Tabla_1_2(models.Model):
    id_job = models.CharField(max_length=30)
    job = models.CharField(max_length=30)
    carpeta = models.CharField(max_length=30)
    proceso = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    com = models.CharField(max_length=30)
    secuencia = models.CharField(max_length=30)
    hora = models.CharField(max_length=30)

class Tabla_2_3(models.Model):
    id_job = models.CharField(max_length=30)
    job = models.CharField(max_length=30)
    carpeta = models.CharField(max_length=30)
    proceso = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    com = models.CharField(max_length=30)
    secuencia = models.CharField(max_length=30)
    hora = models.CharField(max_length=30)

class Tabla_3_4(models.Model):
    id_job = models.CharField(max_length=30)
    job = models.CharField(max_length=30)
    carpeta = models.CharField(max_length=30)
    proceso = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    com = models.CharField(max_length=30)
    secuencia = models.CharField(max_length=30)
    hora = models.CharField(max_length=30)

class Tabla_4_5(models.Model):
    id_job = models.CharField(max_length=30)
    job = models.CharField(max_length=30)
    carpeta = models.CharField(max_length=30)
    proceso = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    com = models.CharField(max_length=30)
    secuencia = models.CharField(max_length=30)
    hora = models.CharField(max_length=30)
    
class Tabla_5(models.Model):
    id_job = models.CharField(max_length=30)
    job = models.CharField(max_length=30)
    carpeta = models.CharField(max_length=30)
    proceso = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    com = models.CharField(max_length=30)
    secuencia = models.CharField(max_length=30)
    hora = models.CharField(max_length=30)
    
class FechaActual(models.Model):
    today = models.DateField()