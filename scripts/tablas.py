"""
Modulo que implementa script para poblar tablas principales
"""

import csv
from pathlib import Path
from datetime import date

from procesos.models import *


BASE_DIR = Path(__file__).resolve().parent.parent


def run():
    """
    Funcion principal del script que pobla la base de datos
    """
    today = date.today()
    today_save = FechaActual(today=today)
    today_save.save()

    tablas = [
        Tabla_23_0,
        Tabla_0_1,
        Tabla_1_2,
        Tabla_2_3,
        Tabla_3_4,
        Tabla_4_5,
        Tabla_5,
    ]

    for i in range(7):
        csv_file_path = BASE_DIR / f"datos/tabla_{i+1}.csv"
        print(csv_file_path)
        # read csv file
        with open(csv_file_path, encoding="utf-8") as csvf:
            reader = csv.reader(csvf)
            next(reader)

            for row_reader in reader:
                print(row_reader)
                row = tablas[i](
                    id_job=row_reader[0],
                    job=row_reader[1],
                    carpeta=row_reader[2],
                    proceso=row_reader[3],
                    tipo=row_reader[4],
                    com=row_reader[5],
                    secuencia=row_reader[6],
                    hora=row_reader[7],
                )
                row.save()
