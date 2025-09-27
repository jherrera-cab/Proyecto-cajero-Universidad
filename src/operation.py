# operaciones.py
from abc import ABC, abstractmethod
import pandas as pd

class Operacion(ABC):
    """Clase abstracta que define la interfaz común para todas las operaciones"""
    
    def __init__(self, data_clientes, data_cuentas, file_cuentas_path):
        self.data_clientes = data_clientes
        self.data_cuentas = data_cuentas
        self.file_cuentas_path = file_cuentas_path

    @abstractmethod
    def ejecutar(self, identificacion):
        pass


class Consignacion(Operacion):
    def ejecutar(self, identificacion, value=None):
        row_client = self.data_clientes[self.data_clientes['Identificacion'] == identificacion]
        if len(row_client) == 0:
            print(f"No se encontró cuenta asociada a la identificación {identificacion}.")
            return
        
        id_cuenta = row_client['ID_cuenta'].values[0]
        row_cuenta = self.data_cuentas[self.data_cuentas['ID_Cuenta'] == id_cuenta]
        #value = int(input("Valor a consignar:\n"))
        last_row = row_cuenta.sort_values('Fecha_operacion', ascending=False)

        if last_row.empty:
            nuevo_saldo = value
        else:
            nuevo_saldo = last_row['Nuevo_saldo'].values[0] + value

        new_operation = {
            'ID_Cuenta': id_cuenta,
            'Saldo' : nuevo_saldo,
            'Tipo_movimiento': 1,
            'valor_movimiento': value,
            'Nuevo_saldo': nuevo_saldo,
            'Fecha_operacion' : pd.Timestamp.now()
        }

        df_cuenta = pd.concat([self.data_cuentas, pd.DataFrame([new_operation])], ignore_index=True)
        df_cuenta.to_csv(self.file_cuentas_path, index=False)
        print(f'Se ha consignado {value} a la cuenta {id_cuenta}.')
        return nuevo_saldo

class Retiro(Operacion):
    def ejecutar(self, identificacion, value=None):
        row_client = self.data_clientes[self.data_clientes['Identificacion'] == identificacion]
        if len(row_client) == 0:
            print(f"No se encontró cuenta asociada a la identificación {identificacion}.")
            return
        
        id_cuenta = row_client['ID_cuenta'].values[0]
        row_cuenta = self.data_cuentas[self.data_cuentas['ID_Cuenta'] == id_cuenta]
        #value = int(input("Valor a retirar:\n"))
        last_row = row_cuenta.sort_values('Fecha_operacion', ascending=False)

        if last_row.empty:
            print("No hay movimientos previos, no se puede retirar.")
            return

        nuevo_saldo = last_row['Nuevo_saldo'].values[0] - value
        if nuevo_saldo < 0:
            print("Saldo insuficiente.")
            return

        new_operation = {
            'ID_Cuenta': id_cuenta,
            'Saldo' : nuevo_saldo,
            'Tipo_movimiento': 2,
            'valor_movimiento': value,
            'Nuevo_saldo': nuevo_saldo,
            'Fecha_operacion' : pd.Timestamp.now()
        }

        df_cuenta = pd.concat([self.data_cuentas, pd.DataFrame([new_operation])], ignore_index=True)
        df_cuenta.to_csv(self.file_cuentas_path, index=False)
        print(f'Se ha retirado {value} de la cuenta {id_cuenta}.')
        return nuevo_saldo

class ConsultaSaldo(Operacion):
    def ejecutar(self, identificacion, value=None):
        row_client = self.data_clientes[self.data_clientes['Identificacion'] == identificacion]
        if len(row_client) == 0:
            return "a1"
        
        id_cuenta = row_client['ID_cuenta'].values[0]
        row_cuenta = self.data_cuentas[self.data_cuentas['ID_Cuenta'] == id_cuenta]
        if row_cuenta.empty:
            print("No movimientos")
            return "a2"
        else:
            saldo = row_cuenta.sort_values("Fecha_operacion", ascending=True)['Saldo'].iloc[-1]
            print(f"{saldo}")
            return saldo
