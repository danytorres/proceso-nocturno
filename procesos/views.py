"""
Views Django
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from procesos.models import FechaActual
from nocturno.helpers.resolve import query_objetos, SaveCountPerHour, ShowCountPerHour
from datetime import datetime, date, time, timedelta


def ActualizarFecha(request):
    date_now = datetime.now()
    t = time(23, 15)
    time_reset = time(00, 00)
    d = date.today()
    # today = datetime.combine(d, t)
    today_reset = datetime.combine(d, time_reset)
    if date_now > today_reset:
        d = d - timedelta(days=1)
    today = datetime.combine(d, t)
    today_objeto = FechaActual.objects.get(id=1)
    today_objeto.today = today
    today_objeto.save()
    return redirect("home_page")


def JobCount(request, segment, work):
    if work == "save":
        SaveCountPerHour(segment)
        tablas_res = []
    elif work == "show":
        tablas_res = ShowCountPerHour(segment)
    else:
        tablas_res = []

    return render(request, "jobs_counts.html", {"tablas_res": tablas_res})


@login_required
def ActualizacionProcesos(request):

    today = FechaActual.objects.all()[0].today

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

    tablas = query_objetos(jobs_rojos)

    return render(
        request, "procesos.html", {"tablas": tablas,
                                   "jobs": jobs_rojos, "fecha": today}
    )
