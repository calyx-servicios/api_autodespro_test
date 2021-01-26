#!/usr/bin/python
import requests
import json
import time

# HEADERS
headers = {
    "Content-type": "application/json",
    "Accept": "*/*",
}
ses = requests.Session()


def _get_move_lines():
    """
    Funcion para obtener los apuntes contables.
    """
    # Setear las variables
    # En este caso solo le pasamos fecha de inicio y fecha de fin
    # Tambien podemos pasar las fechas junto al id o el id solo
    data = {
        "jsonrpc": "2.0",
        "params": {
            "date_from": "01/01/2021",
            "date_to": "10/01/2021",
            # "number": "<numero>" traera los asientos con un id mayor o igual al numero seteado
        },
    }

    # Definir la ruta
    url = "http://5.56.58.182:8069/get_move_line"

    # Realizar la peticion con metodo GET
    # agregamos el "ses" para asignar las cookies
    response = ses.get(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        print(response.content)
    else:
        print("Ocurrio un error.")


def _get_account_moves():
    """
    Funcion para obtener los datos de la facturas.
    """
    # Setear las variables
    # En este caso solo le pasamos fecha de inicio y fecha de fin
    # Tambien podriamos buscar por id
    data = {
        "jsonrpc": "2.0",
        "params": {
            "date_from": "01/01/2020",
            "date_to": "30/12/2020",
            # "id": "<numero>" traera los asientos con un id mayor o igual al numero seteado
        },
    }

    # Definir la ruta
    url = "http://5.56.58.182:8069/get_account_moves"

    # Realizar la peticion con metodo GET
    # agregamos el "ses" para asignar las cookies
    response = ses.get(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        print(response.content)
    else:
        print("Ocurrio un error.")


# Link del sistema, en este caso el que fue proporcionado para pruebas en la V12
# Se agrega el metodo de odoo /web/session/authenticate para inicio de sesion
url = "http://5.56.58.182:8069/web/session/authenticate"

# Setea las variables de inicio de sesion

data = """
    {
    "jsonrpc": "2.0",
    "params":
        {
        "db":"dommo_pruebas",
        "login": "matiastijera@pgyk.com.ar",
        "password": "Autodespro"
        }
    }
"""

#  Realizar la autorizacion mediante un metodo POST
# Agregamos el metodo session para almacenar las cookies y el id de la session
response = ses.post(url, data=data, headers=headers)

# Verificamos si esta correcto el inicio de sesion
print("Conectando...")
time.sleep(0.5)
print("...")
time.sleep(0.5)
print("..")
time.sleep(0.5)
print(".")
time.sleep(0.5)
if response.status_code == 200:
    print("Conexion exitosa.")
    time.sleep(0.5)
    _get_move_lines()  # -> Apuntes contables
    # _get_account_moves()  # -> Facturas

else:
    print("Error")
