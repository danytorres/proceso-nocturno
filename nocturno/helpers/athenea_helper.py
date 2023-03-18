"""
Modulo que ayuda a conectarce con athena
"""

import time
import boto3


def get_var_char_values(d):
    """
    Funcion que devuelve el valor en char
    """
    return [obj["VarCharValue"] for obj in d["Data"]]


def get_data(config):
    """Devuelve los datos de athena de la tablas comparativa

    Args:
        config (List): Lista de parametros para la conexion a athena AWS

    Returns:
        List: Lista de datos obtenidos por el query mandado
    """

    print("Obteniendo datos de athena")
    client = boto3.client(
        "athena",
        aws_access_key_id=config["access"],
        aws_secret_access_key=config["secret"],
        config=config["config"],
    )

    response_query_execution_id = client.start_query_execution(
        QueryString=config["query"],
        QueryExecutionContext={"Database": "default"},
        ResultConfiguration={"OutputLocation": config["location"]},
    )

    response_get_query_details = client.get_query_execution(
        QueryExecutionId=response_query_execution_id["QueryExecutionId"]
    )

    status = "STARTING"
    iterations = 360  # 30 mins
    print(status)

    while iterations > 0:
        iterations = iterations - 1
        response_get_query_details = client.get_query_execution(
            QueryExecutionId=response_query_execution_id["QueryExecutionId"]
        )
        status = response_get_query_details["QueryExecution"]["Status"]["State"]
        print(status)

        if (status == "FAILED") or (status == "CANCELLED"):
            failure_reason = response_get_query_details["QueryExecution"]["Status"][
                "StateChangeReason"
            ]
            print(failure_reason)
            return [{"fallo": failure_reason}]

        elif status == "SUCCEEDED":
            location = response_get_query_details["QueryExecution"][
                "ResultConfiguration"
            ]["OutputLocation"]
            print(f"Location: {location}")

            # Function to get output results
            response_query_result = client.get_query_results(
                QueryExecutionId=response_query_execution_id["QueryExecutionId"]
            )
            result_data = response_query_result["ResultSet"]

            if len(result_data["Rows"]) > 1:
                # header = result_data["Rows"][0]
                rows = result_data["Rows"][1:]

                # header = [obj["VarCharValue"] for obj in header["Data"]]
                # result = [dict(zip(header, get_var_char_values(row))) for row in rows]
                result = [get_var_char_values(row) for row in rows]
                return result
            else:
                header = response_query_result["ResultSet"]["Rows"][0]
                header = [obj["VarCharValue"] for obj in header["Data"]]
                return header
        else:
            time.sleep(2)
