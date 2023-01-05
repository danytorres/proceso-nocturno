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
    today = models.DateTimeField()
    
class Tabla_t001l_erp(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_mara(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_tlog_x(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_tstat(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_mean(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_lfa1(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_tlogf(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_t161t(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_ekko(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_ekbe(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_knop(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_fret(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_ekpo(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_vbrk(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_vbrp(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_val_vb(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.FloatField()
    second_store = models.FloatField()
    
class Tabla_mseg(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.TextField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_trans_1(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_trans_2(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_trans_3(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    trans_colum = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_trans_4(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    trans_colum = models.IntegerField()
    second_store = models.FloatField()
    
class Tabla_trans_5(models.Model):
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    trans_colum = models.IntegerField()
    trans_colum_2 = models.IntegerField()
    second_store = models.FloatField()