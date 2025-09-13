"""
clientes.py
===========

Este módulo implementa la lógica para la gestión de clientes y operaciones bancarias.

Funcionalidades:
----------------
- Crear un nuevo cliente y su cuenta asociada.
- Realizar consignaciones y retiros en cuentas existentes.
- Consultar el saldo de una cuenta por identificación.

Clases:
-------
- new_client:
    - Permite crear un nuevo cliente y guardar sus datos en el archivo correspondiente.
- manatgement_client:
    - Métodos:
        - consignation(identificacion): Consigna dinero en la cuenta asociada.
        - withdrawal(identificacion): Retira dinero de la cuenta asociada.
        - query_client(identificacion): Consulta el saldo de la cuenta asociada.

Entradas:
---------
- Datos personales del cliente.
- Identificación del cliente.
- Valor a consignar o retirar.

Dependencias:
-------------
- pandas
- data_clientes.Read_Cliente

"""

from data.data_clientes import Read_Cliente
import pandas as pd
from src.operation import Operacion
class new_client():
    def __init__(self, Nombres, Apellidos, Identificacion, Movil, Correo, tipo_cuenta):
        self.Nombres = Nombres
        self.Apellidos = Apellidos
        self.Identificacion = Identificacion
        self.Movil = Movil
        self.Correo = Correo
        self.tipo_cuenta = tipo_cuenta
        
    def create_client(self):
        reader = Read_Cliente()
        df_client, df_cuenta = reader.read_data()
        id_client = df_client['ID_cliente'].iloc[-1] + 1
        ID_cuenta = df_client['ID_cuenta'].iloc[-1] + 1

        
        new_row_client = {
            'Nombres': self.Nombres,
            'Apellidos': self.Apellidos,
            'Identificacion': self.Identificacion,
            'Movil': self.Movil,
            'Correo': self.Correo,
            'Tipo cuenta': self.tipo_cuenta,
            'ID_cliente' : id_client,
            'ID_cuenta': ID_cuenta
        }

        df_client = pd.concat([df_client, pd.DataFrame([new_row_client])], ignore_index=True)
        df_client.to_csv(reader.file_clientes_path, index=False)
        print('Se creo correctamete el cliente con identificacion:', self.Identificacion)


class manatgement_client():
    def __init__(self):
        self.read_data = Read_Cliente()
        self.data_clientes, self.data_cuentas = self.read_data.read_data()
        
    def realizar_operacion(self, identificacion, operacion: "Operacion"):
        operacion(self.data_clientes, self.data_cuentas, self.read_data.file_cuentas_path).ejecutar(identificacion)