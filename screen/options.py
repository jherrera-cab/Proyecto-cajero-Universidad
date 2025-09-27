import tkinter as tk
from tkinter import ttk
from screen.create import create_client
from screen.operations import operations_account

def window_options_func(previous_window=None, status= None, id_user=None):
    options = tk.Toplevel(previous_window)
    options.title("Opciones")
    options.geometry("400x300")
    
    ttk.Label(options, text="Seleccione una operación", font=("Arial", 12, "bold")).pack(pady=(15, 5))
    
    if status == "a1":
        ttk.Label(options, text="No se encontró cliente con esa identificación.\n Es necesario crear nuevo cliente.", foreground="red").pack(pady=(5, 5))
        state_button = "create"
    elif status == "a2":
        ttk.Label(options, text="No se encontraron movimientos en la cuenta", foreground="red").pack(pady=(5, 5))   
        state_button = "exists"
    else:
        ttk.Label(options, text=f"Saldo actual: {status}", foreground="green").pack(pady=(5, 5))
        state_button = "exists"
        
    frame_buttons = ttk.Frame(options)
    frame_buttons.pack(pady=10, padx=10)
    
    
    width_button = 20

    def option_operation(type_operation=None):
        
        options.withdraw()
        
        if type_operation == 'create':
            create_client(previous_window=options, main_window=previous_window)
        else:
            operations_account(previous_window=options, 
                               main_window=previous_window, 
                               type_operation=type_operation, 
                               id_user=id_user)

        
    button_create = ttk.Button(frame_buttons, 
                               text="Crear Cliente",
                               width=width_button,
                               command= lambda: option_operation('create'),
                               state="normal" if state_button == "create" else "disabled"
                               ).pack(pady=5, padx=10)
    
    button_deposit = ttk.Button(frame_buttons, 
                                text="Depositar dinero", 
                                width=width_button, 
                                command= lambda: option_operation('deposit'),
                                state="normal" if state_button == "exists" else "disabled"
                                ).pack(pady=5, padx=10)
    
    button_withdraw = ttk.Button(frame_buttons, 
                                 text="Retirar dinero", 
                                 width=width_button,
                                 command= lambda: option_operation('withdraw'),
                                 state="normal" if state_button == "exists" else "disabled"
                                 ).pack(pady=5, padx=10)
    
    button_query = ttk.Button(frame_buttons, 
                              text="Consultar saldo", 
                              width=width_button,
                              command= lambda: option_operation('query'),
                              state="normal" if state_button == "exists" else "disabled"
                              ).pack(pady=5, padx=10)
    
    button_exit = ttk.Button(frame_buttons, 
                             text="Salir", 
                             width=width_button, 
                             command=options.quit
                             ).pack(pady=(15, 5), padx=10)
    
