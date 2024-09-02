import tkinter as tk

"""
Ejemplo 5: Cambiar el Color de Fondo
Este ejemplo permite al usuario cambiar el color de fondo de la ventana utilizando botones.

"""

# Funciones
def cambiar_color(color):
    root.config(bg=color)




root = tk.Tk()

root.title("Cambio de colores")
root.geometry("400x500")


colores = ["red", "green", "blue", "yellow", "white"]

for color in colores:
    button = tk.Button(root, text=color.capitalize(), command=lambda c=color: cambiar_color(c))
    button.pack(side=tk.LEFT, padx=5, pady=5)







root.mainloop()