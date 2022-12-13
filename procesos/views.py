from django.shortcuts import render, redirect
from procesos.models import *
from nocturno.helpers.mysql_helper import mysql_consultor
from datetime import timedelta, datetime, date, time
from django.utils.timezone import make_aware
#from django.conf import settings

# Create your views here.
def ActualizarFecha(request):
    t = time(13, 15)
    d = date.today()
    today_out = datetime.combine(d,t)
    today = make_aware(today_out)
    today_objeto = FechaActual.objects.get(id=1)
    today_objeto.today = today
    today_objeto.save()
    return redirect("home_page")


def ActualizacionProcesos(request):
    tabla_1_q = Tabla_23_0.objects.all()
    tabla_2_q = Tabla_0_1.objects.all()
    tabla_3_q = Tabla_1_2.objects.all()
    tabla_4_q = Tabla_2_3.objects.all()
    tabla_5_q = Tabla_3_4.objects.all()
    tabla_6_q = Tabla_4_5.objects.all()
    tabla_7_q = Tabla_5.objects.all()

    tablas_array = [
        tabla_1_q,
        tabla_2_q,
        tabla_3_q,
        tabla_4_q,
        tabla_5_q,
        tabla_6_q,
        tabla_7_q,
    ]

    # today = date.today()
    # fecha = today.strftime("%Y-%m-%d")
    today = FechaActual.objects.all()[0].today
    man = today + timedelta(days=1)
    fecha_1 = today.strftime("%Y-%m-%d")
    fecha_2 = man.strftime("%Y-%m-%d")
    #print(fecha_1)
    #print(fecha_2)
    #fecha_1 = "2022-09-17"
    #fecha_2 = "2022-09-18"
    datos_actualizados, datos_otros_procesos = mysql_consultor(fecha_1, fecha_2)
    #neva_tabla_1, nueva_tabla_2 = ScriptActualizadoFechas(fecha_1)
    res = []
    for tabla in tablas_array:
        tabla_res = [
            [
                row.id_job,
                row.job,
                row.carpeta,
                row.proceso,
                row.tipo,
                row.com,
                row.secuencia,
                row.hora,
                datos_actualizados.get(
                    int(row.id_job) if row.id_job != "#N/D" else "0",
                    datos_otros_procesos.get(
                        int(row.id_job) if row.id_job != "#N/D" else "0", "sin datos"
                    ),
                ),
            ]
            for row in tabla
        ]
        res.append(tabla_res)

    jobs_rojos = [
        "t001l",
        "mara",
        "posdw_tlogf",
        "posdw_tlogf_x",
        "posdw_tstat",
        "viajes_ingresos",
        "wrf_matgrp_prod",
        "trafico",
        "lfa1",
        "BI_Ext_MEAN",
        "BI_Ext_T161T",
        "vbrk",
        "vbrp",
        "makt",
        "ekko",
        "ekpo",
        "BI_Ext_EKBE",
        "BI_Ext_FRET",
        "BI_Ext_KONP",
        "trafico_ecomm",
        "mseg",
    ]

    tablas = [
        [res[0], "23-0"],
        [res[1], "0-1"],
        [res[2], "1-2"],
        [res[3], "2-3"],
        [res[4], "3-4"],
        [res[5], "4-5"],
        [res[6], "5"],
    ]
    return render(request, "procesos.html", {"tablas": tablas, "jobs": jobs_rojos, "fecha":today})
