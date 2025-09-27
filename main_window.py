import tkinter as tk
from tkinter import ttk
from screen.options import window_options_func
from src.clientes import new_client, manatgement_client
from src.operation import ConsultaSaldo, Consignacion, Retiro
import os

window = tk.Tk()
window.title("Cajero Automático")
window.geometry("400x300")
window.resizable(False, False)


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=5)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)


window.rowconfigure(0, weight=1)
window.rowconfigure(7, weight=1)

label_login_title = ttk.Label(window, text="Bienvenido al sistema bancario")
label_login_title.grid(row=1, column=2, sticky='s', pady=(10,5))

label_login_id = ttk.Label(window, text="Usuario/CC")
label_login_id.grid(row=2, column=2, sticky='s', pady=(10,5))

id_user = tk.StringVar()
text_box = ttk.Entry(window, textvariable=id_user)
text_box.grid(row=6, column=2, padx=5, pady=5)

label_error = ttk.Label(window, text="", foreground="red")
label_error.grid(row=5, column=2, sticky='n', pady=(5,10))

client = manatgement_client()

def login(id_user):
    
    try:
        id_user = int(id_user.get())
        window.withdraw()
        status = client.realizar_operacion(id_user, ConsultaSaldo)
        window_options_func(window, status=status, id_user=id_user)
        
    except ValueError:
        label_error.config(text="Por favor ingrese un número válido.")
        id_user.set("")
        
button_login_start = ttk.Button(window, text="Ingresar", command=lambda: login(id_user))
button_login_start.grid(row=7, column=1, padx=10)

button_login_exit = ttk.Button(window, text="Salir", command=window.quit)
button_login_exit.grid(row=7, column=3, padx=10)

window.mainloop()