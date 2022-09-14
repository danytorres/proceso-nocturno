import mysql.connector
from nocturno.settings import env
from nocturno.helpers.script_sql import ScriptActualizado

def mysql_consultor(fecha):

    script = ScriptActualizado(fecha)
    try:
        conn = mysql.connector.connect(
            host=env("ENDPOINT"),
            user=env("USER"),
            passwd=env("PASSWD"),
            port=env("PORT"),
            database=env("DBNAME"),
        )
        cur = conn.cursor()
        cur.execute(script)
        query_results = cur.fetchall()
        print(query_results)
        return query_results
    except Exception as e:
        print("Database connection failed due to {}".format(e))
        return []
        
