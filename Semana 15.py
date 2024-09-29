import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END
class TaskManager:
    def __init__(self, master):
        self.master = master
        master.title("Gestor de Tareas")
        # Campo de entrada para nuevas tareas
        self.task_input = tk.Entry(master, width=50)
        self.task_input.pack(pady=10)
        self.task_input.bind("<Return>", self.add_task)
        # Botón para añadir tarea
        self.add_button = tk.Button(master, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)
        # Lista de tareas
        self.task_list = Listbox(master, width=50, height=10)
        self.task_list.pack(pady=10)
        # Barra de desplazamiento para la lista
        self.scrollbar = Scrollbar(master)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_list.yview)
        # Botón para marcar como completada
        self.complete_button = tk.Button(master, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)
        # Botón para eliminar tarea
        self.delete_button = tk.Button(master, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)
    def add_task(self, event=None):
        task = self.task_input.get()
        if task:
            self.task_list.insert(END, task)
            self.task_input.delete(0, END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")
    def complete_task(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            completed_task = self.task_list.get(selected_task_index)
            self.task_list.delete(selected_task_index)
            self.task_list.insert(selected_task_index, f"{completed_task} (Completada)")
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para marcar como completada.")
    def delete_task(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminar.")
if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager(root)
    root.mainloop()