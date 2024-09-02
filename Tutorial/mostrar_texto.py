import tkinter as tk


def mostrar_texto():
    texto_entero = entry.get()
    label.config(text=texto_entero)


root = tk.Tk()

"""
Ejemplo 2: Entrada de Texto y Mostrar en Label
Este ejemplo muestra cómo tomar una entrada de texto del usuario y mostrarla en un Label.

"""

root.title("Entrada de texto con Tkinder")
root.geometry("400x200")

# Crear widgets
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

button = tk.Button(root, text="Mostrar Texto", command= mostrar_texto)
button.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=10)


root.mainloop()
