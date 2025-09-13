"""
main.py
========

Este módulo implementa la interfaz principal para el sistema de gestión de clientes de un cajero bancario.

Funcionalidades:
----------------
- Crear un nuevo cliente y su cuenta asociada.
- Consultar el saldo de una cuenta por identificación.
- Consignar dinero en una cuenta existente.
- Retirar dinero de una cuenta existente.

Uso:
----
Al ejecutar el script, se muestra un menú interactivo en consola donde el usuario puede seleccionar la operación deseada.

Clases utilizadas:
------------------
- new_client: Permite crear un nuevo cliente.
- manatgement_client: Permite consultar saldo, consignar y retirar dinero.

Entradas:
---------
- Identificación del cliente (CC)
- Datos personales para la creación de cliente
- Valor a consignar o retirar



"""

from src.clientes import new_client, manatgement_client
import os
from src.operation import ConsultaSaldo, Consignacion, Retiro

while True:
   # os.system('cls')  # Limpia la consola en Windows
    print("Bienvenido al sistema de gestión de clientes.")
    Identificacion = int(input("CC:\n"))
    print("Indique que operacion desea realizar:")
    print("1. Crear cliente")
    print("2. Consultar saldo")
    print("3. Consignar dinero")
    print("4. Retirar dinero")
    
    opcion = input("Seleccione una opción:\n")
    try:
        opcion = int(opcion)
    except ValueError:
        print("Por favor ingrese un número válido.")
        continue
    client = manatgement_client()
    if opcion == 1:
        print("Crear cliente")
        
        nombre = input("Nombres:\n")
        apellido = input("Apellidos:\n")
        movil = int(input("Movil:\n"))
        correo = input("Correo:\n")
        tipo_cuenta = input("Tipo de cuenta:\n")

        client = new_client(
            Nombres=nombre,
            Apellidos=apellido, 
            Identificacion=Identificacion,
            Movil=movil,
            Correo=correo,
            tipo_cuenta=tipo_cuenta
        )
        client.create_client()
    elif opcion == 2:
        client.realizar_operacion(Identificacion, ConsultaSaldo)
    
    elif opcion == 3:
        client.realizar_operacion(Identificacion, Consignacion)
        
    elif opcion == 4:
        client.realizar_operacion(Identificacion, Retiro)