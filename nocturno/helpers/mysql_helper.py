import mysql.connector
from sshtunnel import open_tunnel
from nocturno.settings import env, ssh_key_pem, ssh_server
from nocturno.helpers.script_sql import ScriptActualizado, ScriptOtrosProcesos


def mysql_consultor(fecha_1, fecha_2):

    script_1 = ScriptActualizado(fecha_1)
    script_2 = ScriptOtrosProcesos(fecha_2)

    try:
        with open_tunnel(
            (ssh_server, 22),
            ssh_username="centos",
            ssh_pkey=ssh_key_pem,
            remote_bind_address=(env("ENDPOINT"), int(env("PORT")))
        ) as tunel:
            print(tunel.local_bind_port)
            print("Se creo tunnel")
            conn = mysql.connector.MySQLConnection(
                host="127.0.0.1",
                user=env("USER"),
                password=env("PASSWD"),
                port=int(tunel.local_bind_port),
                database=env("DBNAME")
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
        return {'error': 'sin datos'}, {'error': 'sin datos'}


def CombertirADiccionario(query_results):

    dict_result = {}

    for row in query_results:
        datos_proceso = {
            'status_bandera': row[1],
            'state': row[2],
            'status_ejec': row[3],
            'store_day': row[4]
        }
        dict_result[row[0]] = datos_proceso

    return dict_result
