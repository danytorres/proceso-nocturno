import mysql.connector
from env import *

def mysql_consultor(script):
    try:
        conn = mysql.connector.connect(
            host=ENDPOINT,
            user=USER,
            passwd=PASSWD,
            port=PORT,
            database=DBNAME,
        )
        cur = conn.cursor()
        cur.execute(script)
        query_results = cur.fetchall()
        print(query_results)
        return query_results
    except Exception as e:
        print("Database connection failed due to {}".format(e))
        return []
        

if __name__ == "__main__":
    mysql_consultor(script_prueba)