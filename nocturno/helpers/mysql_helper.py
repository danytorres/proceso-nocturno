import mysql.connector
from nocturno.settings import env
from nocturno.helpers.script_sql import ScriptActualizado, ScriptOtrosProcesos #, ScriptActualizadoFechas


def mysql_consultor(fecha_1, fecha_2):

    script_1 = ScriptActualizado(fecha_1)
    script_2 = ScriptOtrosProcesos(fecha_2)
    #script_3, script_4 = ScriptActualizadoFechas(fecha_1)
    #print(script_3)
    #print(script_4)
    try:
        conn = mysql.connector.connect(
            host=env("ENDPOINT"),
            user=env("USER"),
            passwd=env("PASSWD"),
            port=env("PORT"),
            database=env("DBNAME"),
        )
        cur = conn.cursor()
        cur.execute("SET time_zone = 'America/Mexico_City';")
        cur.execute(script_1)
        query_results_1 = cur.fetchall()
        dict_script_1 = CombertirADiccionario(query_results_1)
        cur.execute(script_2)
        query_results_2 = cur.fetchall()
        dict_script_2 = CombertirADiccionario(query_results_2)
        cur.close()
        return dict_script_1, dict_script_2
    except Exception as e:
        print("Database connection failed due to {}".format(e))
        return [], []
    
def CombertirADiccionario(query_results):
    dict_result = {}
    for row in query_results:
        datos_proceso = {'status_bandera':row[1], 'state': row[2], 'status_ejec':row[3], 'store_day':row[4]}
        dict_result[row[0]] = datos_proceso
    return dict_result
        
