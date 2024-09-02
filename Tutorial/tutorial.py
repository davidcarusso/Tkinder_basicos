import tkinter as tk


"""
Paso 2: Crear la Ventana Principal
Creamos una instancia de la clase Tk, que representará nuestra ventana principal.

"""


root = tk.Tk()

"""
Paso 3: Configurar la Ventana Principal
Podemos configurar algunas propiedades de la ventana, como el título y el tamaño inicial.

"""

root.title("Mi primera app con Tk")
root.geometry("400x500")    # agrega una medida a la ventano


"""

Paso 4: Crear un Widget Label
Un Label es un widget que muestra texto en la ventana. Creamos un Label y lo añadimos a la ventana principal.

tk.Label(root, text="¡Hola Mundo!"): Crea una etiqueta con el texto "¡Hola Mundo!".
label.pack(pady=20): Usa el método pack para colocar la etiqueta en la ventana y 
añade espacio vertical alrededor de la etiqueta."""

label = tk.Label(root, text="Hola mundo!!")
label.pack(pady=20)     #añade un espacio alrededor del widget

"""
Paso 5: Crear una Función para el Evento del Botón
Creamos una función que se ejecutará cuando se haga clic en el botón. Esta función cambiará el texto del Label.
"""

def click_buton():
    label.config(text="Hola Tkinder Boton")

"""
label.config(text="¡Hola, Tkinter!"): Cambia el texto de la etiqueta a "¡Hola, Tkinter!".
"""


"""
Paso 6: Crear un Widget Button
Creamos un botón que llamará a la función click_button cuando se haga clic en él.

"""

boton = tk.Button(root, text="Haz click aqui", command=click_buton)
boton.pack(pady=10)

"""
tk.Button(root, text="Haz clic aquí", command=click_button): 
Crea un botón con el texto "Haz clic aquí" y asocia el evento de clic con la función click_button.

button.pack(pady=10): Usa el método pack para colocar el botón en la ventana y 
añade espacio vertical alrededor del botón.
"""


"""
Paso 7: Ejecutar el Bucle Principal
Finalmente, ejecutamos el bucle principal de la ventana para que permanezca abierta y responda a eventos.
"""


root.mainloop()

"""
root.mainloop(): Inicia el bucle principal de la aplicación. Esto mantiene la ventana abierta y permite la interacción con los widgets.

"""



