from procesos.models import *
from nocturno.helpers.mysql_helper import mysql_consultor
from datetime import date, timedelta


def actualiza_fecha(today):
    today_str = today.strftime("%Y-%m-%d")
    print(f"Actualizar_fecha: {today_str}")
    FechaActual.objects.all().delete()
    objeto_today = FechaActual(today=today)
    objeto_today.save()
    today_res = FechaActual.objects.all()[0].today
    today_str = today_res.strftime("%Y-%m-%d")
    print(f"Fecha en base de datos: {today_str}")
    return {"fecha":today_res}

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
    #fecha_1 = "2022-09-17"
    #fecha_2 = "2022-09-18"
    
    datos_actualizados, datos_otros_procesos = mysql_consultor(fecha_1, fecha_2)
    sin_datos = {'status_bandera':'Sin datos', 'state': 'Sin datos', 'status_ejec':'Sin datos', 'store_day':today}
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
