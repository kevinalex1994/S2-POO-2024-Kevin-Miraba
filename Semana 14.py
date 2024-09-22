import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# TreeView para mostrar la lista de eventos o tareas
tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show='headings')
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(pady=10, padx=10)

# Etiquetas y campos de entrada
lbl_fecha = tk.Label(root, text="Fecha:")
lbl_fecha.pack(padx=5, pady=5)
fecha_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
fecha_entry.pack(padx=5, pady=5)

lbl_hora = tk.Label(root, text="Hora:")
lbl_hora.pack(padx=5, pady=5)
hora_entry = tk.Entry(root)
hora_entry.pack(padx=5, pady=5)

lbl_desc = tk.Label(root, text="Descripción:")
lbl_desc.pack(padx=5, pady=5)
desc_entry = tk.Entry(root)
desc_entry.pack(padx=5, pady=5)

# Función para agregar un nuevo evento
def agregar_evento():
    fecha = fecha_entry.get()
    hora = hora_entry.get()
    descripcion = desc_entry.get()
    if fecha and hora and descripcion:
        tree.insert("", tk.END, values=(fecha, hora, descripcion))
        # Limpiar los campos de entrada
        fecha_entry.delete(0, tk.END)
        hora_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos antes de agregar un evento.")

# Función para eliminar el evento seleccionado
def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        confirm = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este evento?")
        if confirm:
            tree.delete(selected_item)
    else:
        messagebox.showwarning("Selección vacía", "Por favor, seleccione un evento para eliminar.")

# Botón para agregar un evento
btn_agregar = tk.Button(root, text="Agregar Evento", command=agregar_evento)
btn_agregar.pack(padx=5, pady=5)

# Botón para eliminar un evento seleccionado
btn_eliminar = tk.Button(root, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.pack(padx=5, pady=5)

# Botón para salir de la aplicación
btn_salir = tk.Button(root, text="Salir", command=root.quit)
btn_salir.pack(padx=5, pady=5)

# Ejecutar la ventana principal
root.mainloop()