import tkinter as tk
from tkinter import messagebox


"""
4. **Números primos:** Escribe una función que tome un número como entrada y 
devuelva True si es un número primo, de lo contrario, devuelve False.

"""

def num_primos(numero: int) -> bool:
    """
    Comprueba si un número es primo.

    Args:
        numero (int): Número a comprobar.

    Returns:
        bool: True si el número es primo, False en caso contrario.
    """
    # Detectar numeros primos
    for i in range(2,numero):

        if numero % i == 0:
            return False
        
    return True
    

# definimos la funcion integradora en Tk
def tk_calculador_primos():
    """
    Función que toma el valor de entrada de la interfaz gráfica,
    comprueba si es primo y muestra el resultado en un cuadro de diálogo.
    
    """
    try:
        numero = int(entry.get())
        resultado = num_primos(numero)

        if resultado == True:
            messagebox.showinfo("Resultado", f"El numero {numero} \nes primo.")
        else:
            messagebox.showinfo("Resultado", f"El numero {numero} \nno es primo.")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido.")


#resolucion_ejercicio_4()

root = tk.Tk()  # inicio

root.title("Detector de Números Primos")
root.geometry("300x200")

# Crear widgets
label = tk.Label(root, text="Ingrese un Numero: ")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Calcular", command=tk_calculador_primos)
button.pack(pady=10)

button_salir = tk.Button(root, text="Salir", command=root.quit)
button_salir.pack(pady=10)



root.mainloop()     # final
