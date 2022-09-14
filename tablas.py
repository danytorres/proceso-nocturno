import csv 
import json
from procesos.models import *

def csv_to_json():
    tablas = [Tabla_23_0, Tabla_0_1, Tabla_1_2, Tabla_2_3, Tabla_3_4, Tabla_4_5]
    fields = ["id_job", "job", "carpeta", "proceso", "tipo", "com", "secuencia", "hora"]
    
    for i in range(6):
        csvFilePath = f'./procesos/helpers/tabla_{i+1}.csv'
        #read csv file
        with open(csvFilePath, encoding='utf-8') as csvf: 
            reader = csv.reader(csvf)
            next(reader)
            
            for rowReader in reader:
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

          
            
if __name__ == "__main__":
    csv_to_json()