import csv
from pathlib import Path
from procesos.models import *

BASE_DIR = Path(__file__).resolve().parent.parent


def run():
    tablas = [
        Tabla_23_0,
        Tabla_0_1,
        Tabla_1_2,
        Tabla_2_3,
        Tabla_3_4,
        Tabla_4_5,
        Tabla_5,
    ]
    # fields = ["id_job", "job", "carpeta", "proceso", "tipo", "com", "secuencia", "hora"]

    for i in range(7):
        csvFilePath = BASE_DIR / f"datos/tabla_{i+1}.csv"
        print(csvFilePath)
        # read csv file
        with open(csvFilePath, encoding="utf-8") as csvf:
            reader = csv.reader(csvf)
            next(reader)

            for rowReader in reader:
                print(rowReader)
                row = tablas[i](
                    id_job=rowReader[0],
                    job=rowReader[1],
                    carpeta=rowReader[2],
                    proceso=rowReader[3],
                    tipo=rowReader[4],
                    com=rowReader[5],
                    secuencia=rowReader[6],
                    hora=rowReader[7],
                )
                row.save()
