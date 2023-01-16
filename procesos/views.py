from django.shortcuts import render, redirect
from procesos.models import *
from nocturno.helpers.athenea_helper import get_data
from nocturno.helpers.resolve import query_objetos, SaveCountPerHour, ShowCountPerHour
from datetime import datetime, date, time
from django.utils.timezone import make_aware
from django.conf import settings
from nocturno.helpers.script_sql_job import scripts_jobs, jobs
from django.core.exceptions import ValidationError, ObjectDoesNotExist

# Create your views here.
def ActualizarFecha(request):
    t = time(13, 15)
    d = date.today()
    today_out = datetime.combine(d, t)
    today = make_aware(today_out)
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

    return render(request, "jobs_counts.html", {"tablas_res": tablas_res})


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
    
    tablas = query_objetos()
    
    return render(
        request, "procesos.html", {"tablas": tablas, "jobs": jobs_rojos, "fecha": today}
    )
