from django.shortcuts import render
from procesos.models import *
from nocturno.helpers.mysql_helper import mysql_consultor
from datetime import date

# Create your views here.
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
    fecha_1 = "2022-09-16"
    fecha_2 = "2022-09-17"
    datos_actualizados, datos_otros_procesos = mysql_consultor(fecha_1, fecha_2)
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

    tabla_1 = res[0]
    tabla_2 = res[1]
    tabla_3 = res[2]
    tabla_4 = res[3]
    tabla_5 = res[4]
    tabla_6 = res[5]
    tabla_7 = res[6]
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
        [tabla_1, "23-0"],
        [tabla_2, "0-1"],
        [tabla_3, "1-2"],
        [tabla_4, "2-3"],
        [tabla_5, "3-4"],
        [tabla_6, "4-5"],
        [tabla_7, "5"],
    ]
    return render(request, "procesos.html", {"tablas": tablas, "jobs": jobs_rojos})
