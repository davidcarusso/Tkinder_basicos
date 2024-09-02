import tkinter as tk
from tkinter import ttk


def show_seleccition():
    seleccion = combobox.get()
    label.config(text=f"Seleccionaste: {seleccion.capitalize()}")
    

root = tk.Tk()

root.title("Listas Desplegables")
root.geometry("300x200")

# Crear widgets
options = ["opcion A", "opcion B", "opcion C"]
combobox = ttk.Combobox(root, values=options)
combobox.pack(pady=10)

button = tk.Button(root, text="Mostrar Seleccion", command=show_seleccition)
button.pack(pady=10)

label = tk.Label(root, text="label")
label.pack(pady=10)




root.mainloop()