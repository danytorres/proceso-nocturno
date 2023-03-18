import boto3
from botocore.config import Config
import csv
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent

ACCESS_KEY = 'ASIAZU4EQF4TYAGLLFPS'
SECRET_KEY = 'GnS6RbECXdmp+MpVfFteUSLsXDc+WovX281KeUqB'
SESSION_TOKEN = 'IQoJb3JpZ2luX2VjEDUaCXVzLWVhc3QtMSJHMEUCIQCAMQRKzPaN3Ur1AOhnM1i1DrifhBJxFFXdA3O4hhd0twIgaFEZTFmRmtGVGqXa9gmoEnmTo12OlJ+XeVW9ErJkjFUqnwMIvv//////////ARAAGgw2NjMzMTM0NjEwMzEiDDO8tNV6RBD+MW4x1irzAg/Hz6D7yZR9kWl5lvqBQ4WUCBd6eK1hFpNoUu5sRuA2YdXVfhd8N6xrWBp7hPigtB2DgYhbecYI58V0mI+rVIgbxV24QhXG63yVpwlzpd1A6DtGZEFwkLqF5pzKygn1BL9xy9dqfqoRhKkizA0QDKh9p+zAzL26tXEvv7qH12V765rN+Wma+Fs04RPy+KLbXW14wlAAT7GfG3SswAcWgmVjqYxqH4UpVrof2jWTJ5hheVKTSg9OpG7zdRh7EFSBpbFol5MpJjarNyR6BNqSudTRj49bUJU0KPQjFGqQvZ5bKQd0LR+N/A8XjNcXNe7OzpLD1JjHyefr/bTOPa2i1K+OJ0V8pCF2FHaDN4/o2H8/4CBmnF7/oLFh+seYKAVugyMD4hWZIm3kALEqE7sUdMvTLflQEsxaj2DSLxruluXVDFzauobQAQP1OazwoifjfZDDCJ+Y2TEcNHxcTjN1zdrKD31eoMe/Xe7J/lw/3D49d3KKMIWXnp8GOqYBTVaSfaQakStPkBod7VPnt/yACFjB25NXG4LHlzkYTCouoq18E5CgbSiAxuxfDifAhaRlqfJB7Nhyb42b0DLMlmFDh3ZIOJw7/Y3YUyRuZs6ajU6sSEbvDlPCoWS5At46oFz3s9RRVl+HipF5XS0auoUW3V2f3YeAEkKnQ58IMenY644WfEV78L3ntBm7g/cXK3Pa+zhMhmQCMxrCuVuQdt4IrORNqQ=='

my_config = Config(
    region_name="us-east-1",
)


def IDinstances():
    # BASE_DIR / f"datos/id.csv"
    csvFilePath = "/Users/danytorres/proceso-nocturno-2/proceso-nocturno/datos/id.csv"
    print(csvFilePath)
    # read csv file
    with open(csvFilePath, encoding="utf-8") as csvf:
        reader = csv.reader(csvf)
        # instances = next(reader)
        reader_list = [id_instance for id_instance in reader]

    # print(type(list(reader_list[0][1:])))
    return [id for id in reader_list[0][1:] if id != ''], reader_list


def ComprobarEstatusMaquinas():
    """hols vvdd"""
    client = boto3.client(
        'ec2',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_session_token=SESSION_TOKEN,
        config=my_config
    )

    reader_list, reader_list_with_no_code = IDinstances()

    ec2_instance = client.describe_instances(InstanceIds=reader_list)
    # [0]['Instances'][0]['State']['Name'] # [5]['Instances'][0]
    datos = ec2_instance['Reservations']

    status_instances = [instance_data['Instances'][0]
                        ['State']['Name'] for instance_data in datos]

    # print(len(datos))
    # print(datos)
    print(status_instances)
    print(json.dumps(ec2_instance))


if __name__ == '__main__':
    ComprobarEstatusMaquinas()
    # reader_list = IDinstances()
