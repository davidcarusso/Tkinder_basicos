import tkinter as tk



root = tk.Tk()

root.title("Uso de Frame")
root.geometry("300x200")



"""
tk.Frame(root, bg="lightblue", bd=5): 
Crea un frame con un fondo azul claro (bg="lightblue") y un borde de 5 píxeles (bd=5). 
Este frame está contenido dentro de root.

frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER): 
Coloca el frame en el centro de la ventana. relx y rely son coordenadas relativas 
(de 0 a 1) que indican la posición del frame en relación con la ventana principal. 
anchor=tk.CENTER alinea el frame en su centro.


"""
#Crear un Frame
frame = tk.Frame(root, bg="lightblue", bd=5)        #bd es borde
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER ) 



# Añadir widgets al frame
label = tk.Label(frame, text="Este es un frame", bg="lightblue")
label.pack(pady=10)

button = tk.Button(root, text="Cerrar", command=root.quit)
button.pack(pady=10)





root.mainloop()