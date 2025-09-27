import tkinter as tk
from tkinter import ttk
from src.clientes import new_client

def create_client(previous_window=None, main_window=None):
    create = tk.Toplevel(previous_window)
    create.title("Crear Cliente")
    create.geometry("400x400")
    create.columnconfigure(0, weight=1)
    create.columnconfigure(1, weight=5)
    create.columnconfigure(2, weight=5)
    create.columnconfigure(3, weight=1)
    
    ttk.Label(create, 
              text="Formulario de creación de cliente", 
              font=("Arial", 12, "bold")
              ).grid(row=0, column=1, columnspan=2, pady=10)

    nombres = tk.StringVar()
    apellidos = tk.StringVar()
    identificacion = tk.StringVar()
    movil = tk.StringVar()  
    correo = tk.StringVar()
    tipo_cuenta = tk.StringVar()
    id_cliente = tk.StringVar()
    
    frame_label = ttk.Frame(create)
    frame_button = ttk.Frame(create)
    frame_label.grid(row=3, column=1, sticky='e')
    frame_button.grid(row=3, column=2, sticky='e')
        
    ttk.Label(frame_label, text="Nombres:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
    ttk.Label(frame_label, text="Apellidos:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
    ttk.Label(frame_label, text="Identificación:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
    ttk.Label(frame_label, text="Móvil:").grid(row=4, column=0, padx=10, pady=10, sticky='e')
    ttk.Label(frame_label, text="Correo:").grid(row=5, column=0, padx=10, pady=10, sticky='e')
    ttk.Label(frame_label, text="Tipo de cuenta:").grid(row=6, column=0, padx=10, pady=10, sticky='e')
    
    ttk.Entry(frame_button, textvariable=nombres).grid(row=1, column=1, padx=10, pady=10)
    ttk.Entry(frame_button, textvariable=apellidos).grid(row=2, column=1, padx=10, pady=10)
    ttk.Entry(frame_button, textvariable=identificacion).grid(row=3, column=1, padx=10, pady=10)
    ttk.Entry(frame_button, textvariable=movil).grid(row=4, column=1, padx=10, pady=10)
    ttk.Entry(frame_button, textvariable=correo). grid(row=5, column=1, padx=10, pady=10)
    ttk.Entry(frame_button, textvariable=tipo_cuenta).grid(row=6, column=1, padx=10, pady=10)
    
    label_info = ttk.Label(create, text="", foreground="green")
    label_info.grid(row=8, column=0, columnspan=2, pady=10)
    
    def save_client():
        client = new_client(
            Nombres=nombres.get(),
            Apellidos=apellidos.get(),
            Identificacion=int(identificacion.get()),       
            Movil=int(movil.get()),
            Correo=correo.get(),
            tipo_cuenta=tipo_cuenta.get()
        )
        print(client)
        status = client.create_client()
        label_info.config(text="Cliente creado exitosamente.")
        
    
        
    ttk.Button(create, text="Guardar", command=lambda: save_client()).grid(row=7, column=1, padx=10, pady=10)
    ttk.Button(create, text="Salir", command=main_window.destroy).grid(row=7, column=2, padx=10, pady=10)
    