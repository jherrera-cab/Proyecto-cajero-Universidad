import tkinter as tk
from tkinter import ttk
from src.clientes import manatgement_client
from src.operation import ConsultaSaldo, Consignacion, Retiro

def operations_account(previous_window=None, main_window=None, type_operation=None, id_user=None):
    create = tk.Toplevel(previous_window)
    create.title("Operacion en cuenta")
    create.geometry("400x400")
    
    ttk.Label(create, 
              text=f"Formulario de {type_operation} en cuenta",
              font=("Arial", 12, "bold")
    ).grid(row=0, column=1, columnspan=2, pady=10)
    
    ttk.Label(create, text="Valor a transaccion:").grid(row=2, column=0, pady=10)
    value_operation = tk.StringVar()
    ttk.Entry(create, textvariable=value_operation).grid(row=2, column=1, columnspan=2, pady=10)
    
    client = manatgement_client()
    def execute_operation():
        if type_operation == "deposit":
            new_balance = client.realizar_operacion(id_user, Consignacion, value=int(value_operation.get()))    
            label_result.config(text=f"Operacion exitosa.\nNuevo saldo: {new_balance}", font=("Arial", 12, "bold"), foreground="green")
        elif type_operation == "withdraw":
            new_balance = client.realizar_operacion(id_user, Retiro, value=int(value_operation.get()))    
            label_result.config(text=f"Operacion exitosa.\nNuevo saldo: {new_balance}", font=("Arial", 12, "bold"), foreground="green")
        elif type_operation == "query":
            current_balance = client.realizar_operacion(id_user, ConsultaSaldo)    
            label_result.config(text=f"Saldo actual: {current_balance}", font=("Arial", 12, "bold"), foreground="green")
    
    label_result = ttk.Label(create, text=f"")
    label_result.grid(row=3, column=0, columnspan=3, pady=10) 
    
    ttk.Button(create, 
               text="Ejecutar operacion", 
               command= execute_operation
    ).grid(row=4, column=1, pady=20)    
    ttk.Button(create, text="Volver", command=lambda: [create.destroy(), previous_window.deiconify()]).grid(row=5, column=1, pady=20)