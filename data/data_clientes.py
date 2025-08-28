
"""
data_clientes.py
================

Este módulo gestiona la lectura de datos de clientes y cuentas bancarias desde archivos CSV.

Funcionalidades:
----------------
- Leer los datos de clientes y cuentas desde rutas especificadas en variables de entorno.
- Manejar errores comunes al leer archivos CSV (archivo no encontrado, archivo vacío, errores de parseo).

Clases:
-------
- Read_Cliente: 
    - Métodos:
        - read_data(): Devuelve dos DataFrames de pandas con los datos de clientes y cuentas.

Entradas:
---------
- Rutas de archivos CSV definidas en variables de entorno:
    - path_clientes
    - path_cuentas

Dependencias:
-------------
- pandas
- python-dotenv
- os
- pathlib

Autor: Tu Nombre
Fecha: 2024

"""

import pandas as pd
from dotenv import load_dotenv
import os
from pathlib import Path


class Read_Cliente:
    def __init__(self):
        load_dotenv()
        path_clientes = os.getenv('path_clientes')
        path_cuentas = os.getenv('path_cuentas')
        self.file_clientes_path = path_clientes
        self.file_cuentas_path = path_cuentas
        
        
    def read_data(self):
        try:
            data_clientes = pd.read_csv(self.file_clientes_path)
            data_cuentas = pd.read_csv(self.file_cuentas_path) 
           
            return data_clientes, data_cuentas
        except FileNotFoundError:
            print(f"Error: The file at {self.file_clientes_path} was not found.")
            print(f"Error: The file at {self.file_cuentas_path} was not found.")
            return None
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            return None
        except pd.errors.ParserError:
            print("Error: There was a parsing error while reading the file.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None