import tkinter as tk


"""
Ejemplo 3: Calculadora Básica
Este ejemplo implementa una calculadora básica que puede sumar dos números.

"""

"""
Logica de calculadora
"""

def calculadora():
    try:
        num1 = float(entrada1.get()) 
        num2 = float(entrada2.get())
        result = num1 + num2
        label_result.config(text=f"Resultado: {result}")
    except ValueError:
        label_result.config(text="Entrada no valida")


# Crear la ventana principal
ventana = tk.Tk()

ventana.title("Calculadora TKinder")
ventana.geometry("300x200")

# Crear widgets
entrada1 = tk.Entry(ventana)    # entrada 1
entrada1.pack(pady=10)

entrada2 = tk.Entry(ventana)    # entrada 2
entrada2.pack(pady=10)

# generamos el boton
boton = tk.Button(ventana, text="Sumar", command=calculadora)
boton.pack(pady=10)

label_result = tk.Label(ventana, text="Resultado: ")
label_result.pack(pady=10)


ventana.mainloop()