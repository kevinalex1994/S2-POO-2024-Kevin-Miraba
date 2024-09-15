import tkinter as tk
from tkinter import messagebox
# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada.get()  # Obtener el dato del campo de texto
    if dato:
        lista.insert(tk.END, dato)  # Agregar el dato a la lista
        entrada.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")
# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)  # Eliminar todos los elementos de la lista
# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")
# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=10)
# Campo de texto
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)
# Botón "Agregar"
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)
# Lista para mostrar datos
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)
# Botón "Limpiar"
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)
# Ejecutar la aplicación
ventana.mainloop()