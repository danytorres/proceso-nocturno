from procesos.models import *
from nocturno.helpers.mysql_helper import mysql_consultor
from datetime import timedelta
from django.conf import settings
from nocturno.helpers.script_sql_job import scripts_jobs, jobs
from nocturno.helpers.athenea_helper import get_data
from django.core.exceptions import ObjectDoesNotExist


def query_objetos():
    
    tablas_dict = {
        'Tabla_23_0':Tabla_23_0.objects.all(),
        'Tabla_0_1':Tabla_0_1.objects.all(),
        'Tabla_1_2':Tabla_1_2.objects.all(),
        'Tabla_2_3':Tabla_2_3.objects.all(),
        'Tabla_3_4':Tabla_3_4.objects.all(),
        'Tabla_4_5':Tabla_4_5.objects.all(),
        'Tabla_5':Tabla_5.objects.all()
        }

    today = FechaActual.objects.all()[0].today
    man = today + timedelta(days=1)
    fecha_1 = today.strftime("%Y-%m-%d")
    fecha_2 = man.strftime("%Y-%m-%d")
    
    datos_actualizados, datos_otros_procesos = mysql_consultor(fecha_1, fecha_2)
    sin_datos = {
        'status_bandera':'Sin datos',
        'state': 'Sin datos',
        'status_ejec':'Sin datos',
        'store_day':today
        }
    res = {}
    for key, tabla in tablas_dict.items():
        list_tabla = []
        for row in tabla:
            status_row = datos_actualizados.get(
                            int(row.id_job) if row.id_job != "#N/D" else "0",
                            datos_otros_procesos.get(
                                int(row.id_job) if row.id_job != "#N/D" else "0", 
                                sin_datos
                            )
                        )
            dict_row = {
                    'id_job':row.id_job,
                    'job':row.job,
                    'carpeta':row.carpeta,
                    'proceso':row.proceso,
                    'tipo':row.tipo,
                    'com':row.com,
                    'secuencia':row.secuencia,
                    'hora':row.hora,
                    'status_bandera':status_row['status_bandera'], 
                    'state': status_row['state'], 
                    'status_ejec':status_row['status_ejec'], 
                    'store_day':status_row['store_day']
                    }
            list_tabla.append(dict_row)
        res[key] = list_tabla

    return res

def Parametros(segment):
    today = FechaActual.objects.all()[0].today
    tablas_base_datos = (
        (Tabla_t001l_erp, Tabla_mara),
        (Tabla_mean, Tabla_lfa1),
        (Tabla_t161t, Tabla_vbrk, Tabla_vbrp, Tabla_val_vb),
        (Tabla_ekko, Tabla_ekbe, Tabla_knop, Tabla_fret, Tabla_ekpo),
        [Tabla_mseg],
        (Tabla_tlog_x, Tabla_tstat, Tabla_tlogf),
    )

    if segment == 0:
        scripts = [x for l in scripts_jobs for x in l]
        rows_seg = 10
        base_datos = [x for l in tablas_base_datos for x in l]
        nombre_bloque = [x for l in jobs for x in l]
        store = False
    else:
        bloque = segment - 1
        scripts = scripts_jobs[bloque]
        rows_seg = 11
        base_datos = tablas_base_datos[bloque]
        nombre_bloque = jobs[bloque]
        store = True
    
    return today, scripts, rows_seg, base_datos, nombre_bloque, store

def SaveCountPerHour(segment):
    today, scripts, rows_seg, base_datos, nombre_bloque, store = Parametros(segment)

    config = settings.CONFIG_DATA_AWS

    for index in range(len(scripts)):
        config["query"] = scripts[index] + f" limit {rows_seg};"
        res_script = get_data(config)

        for row in res_script:
            try:
                obj_to_save = base_datos[index](
                    day_process=today,
                    storeday_colum=row[0],
                    count=row[1],
                    second_store=store,
                )
                obj_to_save.save()
                print(f"guardando row en {nombre_bloque[index]}")
            except:
                print("error guardando objeto")

def ShowCountPerHour(segment):
    today, scripts, rows_seg, base_datos, nombre_bloque, store = Parametros(segment)
    tablas_res = []
    for index in range(len(base_datos)):
        all_obj_after = base_datos[index].objects.filter(
            day_process=today, second_store=True
        )
        nombre_tabla = nombre_bloque[index]
        tabla_gen = []
        for data in all_obj_after:
            try:
                obj_before = (
                    base_datos[index].objects.get(
                        day_process=today,
                        second_store=False,
                        storeday_colum=data.storeday_colum,
                    )
                    if len(all_obj_after) != 1
                    else base_datos[index].objects.get(
                        day_process=today, second_store=False
                    )
                )
                before_count = obj_before.count
                before_storeday = obj_before.storeday_colum
            except ObjectDoesNotExist:
                before_count = 0
                before_storeday = data.storeday_colum

            try:
                diferencia = data.count - before_count
                porcentaje = "{0:.2%}".format(diferencia / data.count)
            except ZeroDivisionError:
                porcentaje = 0
                
            row = [
                before_storeday,
                before_count,
                data.storeday_colum,
                data.count,
                diferencia,
                porcentaje,
            ]

            tabla_gen.append(row)

        tablas_res.append([nombre_tabla, tabla_gen])
    
    return tablas_res