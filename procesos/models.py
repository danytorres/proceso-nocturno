"""
Models Django
"""

from django.db import models


class BanderaSaveJobs(models.Model):
    """
    Tabla para
    """
    job = models.CharField(max_length=30)
    day_process = models.DateTimeField()
    status_bandera = models.CharField(max_length=30)


class Tabla_23_0(models.Model):
    """
    Tabla para guardas jobs de la primera hora
    """
    id_job = models.CharField(max_length=70)
    job = models.CharField(max_length=70)
    carpeta = models.CharField(max_length=70)
    proceso = models.CharField(max_length=70)
    tipo = models.CharField(max_length=70)
    com = models.CharField(max_length=70)
    secuencia = models.CharField(max_length=70)
    hora = models.CharField(max_length=70)


class Tabla_0_1(models.Model):
    """
    Tabla para guardas jobs de la segunda hora
    """
    id_job = models.CharField(max_length=70)
    job = models.CharField(max_length=70)
    carpeta = models.CharField(max_length=70)
    proceso = models.CharField(max_length=70)
    tipo = models.CharField(max_length=70)
    com = models.CharField(max_length=70)
    secuencia = models.CharField(max_length=70)
    hora = models.CharField(max_length=70)


class Tabla_1_2(models.Model):
    """
    Tabla para guardas jobs de la tercera hora
    """
    id_job = models.CharField(max_length=70)
    job = models.CharField(max_length=70)
    carpeta = models.CharField(max_length=70)
    proceso = models.CharField(max_length=70)
    tipo = models.CharField(max_length=70)
    com = models.CharField(max_length=70)
    secuencia = models.CharField(max_length=70)
    hora = models.CharField(max_length=70)


class Tabla_2_3(models.Model):
    """
    Tabla para guardas jobs de la cuarta hora
    """
    id_job = models.CharField(max_length=70)
    job = models.CharField(max_length=70)
    carpeta = models.CharField(max_length=70)
    proceso = models.CharField(max_length=70)
    tipo = models.CharField(max_length=70)
    com = models.CharField(max_length=70)
    secuencia = models.CharField(max_length=70)
    hora = models.CharField(max_length=70)


class Tabla_3_4(models.Model):
    """
    Tabla para guardas jobs de la quinta hora
    """
    id_job = models.CharField(max_length=70)
    job = models.CharField(max_length=70)
    carpeta = models.CharField(max_length=70)
    proceso = models.CharField(max_length=70)
    tipo = models.CharField(max_length=70)
    com = models.CharField(max_length=70)
    secuencia = models.CharField(max_length=70)
    hora = models.CharField(max_length=70)


class Tabla_4_5(models.Model):
    """
    Tabla para guardas jobs de la sexta hora
    """
    id_job = models.CharField(max_length=70)
    job = models.CharField(max_length=70)
    carpeta = models.CharField(max_length=70)
    proceso = models.CharField(max_length=70)
    tipo = models.CharField(max_length=70)
    com = models.CharField(max_length=70)
    secuencia = models.CharField(max_length=70)
    hora = models.CharField(max_length=70)


class Tabla_5(models.Model):
    """
    Tabla para guardas jobs de la septima hora
    """
    id_job = models.CharField(max_length=70)
    job = models.CharField(max_length=70)
    carpeta = models.CharField(max_length=70)
    proceso = models.CharField(max_length=70)
    tipo = models.CharField(max_length=70)
    com = models.CharField(max_length=70)
    secuencia = models.CharField(max_length=70)
    hora = models.CharField(max_length=70)


class FechaActual(models.Model):
    """
    Tabla fecha actual del proceso
    """
    today = models.DateTimeField()


class Tabla_t001l_erp(models.Model):
    """
    Tabla para guardar info t001l
    """
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_mara(models.Model):
    """
    Tabla para guardar info mara
    """
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_tlog_x(models.Model):
    """
    Tabla para guardar info tlog_x
    """
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_tstat(models.Model):
    """
    Tabla para guardar info tstat
    """
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_mean(models.Model):
    """
    Tabla para guardar info mean
    """
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_lfa1(models.Model):
    """
    Tabla para guardar info lfa1
    """
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_tlogf(models.Model):
    """
    Tabla para guardar info tlogf
    """
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_t161t(models.Model):
    """
    Tabla para guardar info t161t
    """
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_ekko(models.Model):
    """
    Tabla para guardar info ekko
    """
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_ekbe(models.Model):
    """
    Tabla para guardar info ekbe
    """
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_knop(models.Model):
    """
    Tabla para guardar info knop
    """
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_fret(models.Model):
    """
    Tabla para guardar info fret
    """
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_ekpo(models.Model):
    """
    Tabla para guardar info ekpo
    """
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_vbrk(models.Model):
    """
    Tabla para guardar info vbrk
    """
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_vbrp(models.Model):
    """
    Tabla para guardar info vbrp
    """
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_val_vb(models.Model):
    """
    Tabla para guardar info val_vb
    """
    day_process = models.DateTimeField()
    storeday_colum = models.IntegerField()
    count = models.FloatField()
    second_store = models.FloatField()


class Tabla_mseg(models.Model):
    """
    Tabla para guardar info mseg
    """
    day_process = models.DateTimeField()
    storeday_colum = models.TextField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_trans_1(models.Model):
    """
    Tabla para guardar info transacciones 1
    """
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_trans_2(models.Model):
    """
    Tabla para guardar info transacciones 2
    """
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    second_store = models.FloatField()


class Tabla_trans_3(models.Model):
    """
    Tabla para guardar info transacciones 3
    """
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    trans_colum = models.IntegerField()
    second_store = models.FloatField()


class Tabla_trans_4(models.Model):
    """
    Tabla para guardar info transacciones 4
    """
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    trans_colum = models.IntegerField()
    second_store = models.FloatField()


class Tabla_trans_5(models.Model):
    """
    Tabla para guardar info transacciones 5
    """
    day_process = models.DateTimeField()
    storeday_colum = models.DateTimeField()
    count = models.IntegerField()
    trans_colum = models.IntegerField()
    trans_colum_2 = models.IntegerField()
    second_store = models.FloatField()
