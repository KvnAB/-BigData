import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import ttkbootstrap as ttkb
import pandas as pd

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Empleados y Rueda de la Vida")

        self.empleados = self.cargar_datos()  # Cargar datos desde JSON

        # Usando ttkbootstrap para aplicar un tema moderno
        self.style = ttkb.Style("flatly")  # Puedes elegir otros estilos como "darkly", "cyborg", etc.

        # Crear menú
        self.crear_menu()

        # Crear pestañas (notebook)
        self.notebook = ttkb.Notebook(root, bootstyle="primary")
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Pestaña de registro
        self.crear_pestana_registro()

        # Pestaña de Rueda de la Vida
        self.crear_pestana_rueda_vida()

        # Pestaña de visualización
        self.crear_pestana_visualizacion()

        # Pestaña de gestión de registros
        self.crear_pestana_gestion_registros()

    def cargar_datos(self):
        """Cargar datos desde un archivo JSON o devolver un diccionario vacío."""
        if os.path.exists("empleados.json"):
            with open("empleados.json", "r") as f:
                return json.load(f)
        return {}

    def guardar_datos(self):
        """Guardar los datos en un archivo JSON."""
        with open("empleados.json", "w") as f:
            json.dump(self.empleados, f, indent=4)

    def crear_menu(self):
        """Crear el menú de la aplicación."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        archivo_menu = tk.Menu(menubar, tearoff=0)
        archivo_menu.add_command(
            label="Exportar a Excel",
            command=self.exportar_a_excel
        )
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.root.quit)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)

    def exportar_a_excel(self):
        """Exportar los datos de los empleados a un archivo Excel."""
        if not self.empleados:
            messagebox.showwarning("Error", "No hay datos para exportar.")
            return

        # Convertir los datos de empleados en un DataFrame
        empleados_data = []
        for nombre, datos in self.empleados.items():
            empleado_info = {
                "Nombre": nombre,
                "Apellido": datos["apellido"],
                "Edad": datos["edad"],
                "Teléfono": datos["telefono"],
                "Email": datos["email"],
                "Carrera": datos["rueda"]["carrera"],
                "Finanzas": datos["rueda"]["finanzas"],
                "Salud": datos["rueda"]["salud"],
                "Familia": datos["rueda"]["familia"],
                "Amor": datos["rueda"]["amor"],
                "Crecimiento": datos["rueda"]["crecimiento"],
                "Diversión": datos["rueda"]["diversion"],
                "Contribución": datos["rueda"]["contribucion"]
            }
            empleados_data.append(empleado_info)

        df = pd.DataFrame(empleados_data)
        df.to_excel("empleados.xlsx", index=False)
        messagebox.showinfo("Exportar", "Datos exportados correctamente a 'empleados.xlsx'.")

    def crear_pestana_registro(self):
        """Crear la pestaña de registro de empleados."""
        frame_registro = ttkb.Frame(self.notebook, padding=20, bootstyle="info")

        # Agregar el frame al notebook
        self.notebook.add(frame_registro, text="Registro de Empleado")

        # Crear los widgets dentro del frame
        ttk.Label(frame_registro, text="Nombre:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_nombre = ttk.Entry(frame_registro, font=('Arial', 10))
        self.entry_nombre.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(frame_registro, text="Apellido:", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_apellido = ttk.Entry(frame_registro, font=('Arial', 10))
        self.entry_apellido.grid(row=1, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(frame_registro, text="Edad:", font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_edad = ttk.Entry(frame_registro, font=('Arial', 10))
        self.entry_edad.grid(row=2, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(frame_registro, text="Número Telefónico:", font=('Arial', 10, 'bold')).grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_telefono = ttk.Entry(frame_registro, font=('Arial', 10))
        self.entry_telefono.grid(row=3, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(frame_registro, text="Email:", font=('Arial', 10, 'bold')).grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_email = ttk.Entry(frame_registro, font=('Arial', 10))
        self.entry_email.grid(row=4, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Button(frame_registro, text="Guardar Registro", bootstyle="success", command=self.guardar_registro).grid(row=5, columnspan=2, pady=10)

    def crear_pestana_rueda_vida(self):
        """Crear la pestaña de Rueda de la Vida."""
        frame_rueda = ttkb.Frame(self.notebook, padding=20, bootstyle="info")

        # Agregar el frame al notebook
        self.notebook.add(frame_rueda, text="Rueda de la Vida")

        ttk.Label(frame_rueda, text="Nombre del empleado:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_nombre_respuestas = ttk.Entry(frame_rueda, font=('Arial', 10))
        self.entry_nombre_respuestas.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)

        self.campos = [
            ("Carrera", "carrera"),
            ("Finanzas", "finanzas"),
            ("Salud", "salud"),
            ("Familia", "familia"),
            ("Amor", "amor"),
            ("Crecimiento", "crecimiento"),
            ("Diversión", "diversion"),
            ("Contribución", "contribucion")
        ]

        for i, (label, attr) in enumerate(self.campos, start=1):
            ttk.Label(frame_rueda, text=f"{label} (1-10):", font=('Arial', 10, 'bold')).grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
            entry = ttk.Entry(frame_rueda, font=('Arial', 10))
            entry.grid(row=i, column=1, sticky=tk.EW, padx=10, pady=5)
            setattr(self, attr, entry)

        ttk.Button(frame_rueda, text="Guardar Respuestas", bootstyle="success", command=self.guardar_respuestas).grid(row=len(self.campos) + 1, columnspan=2, pady=10)

    def crear_pestana_visualizacion(self):
        """Crear la pestaña de visualización de datos."""
        frame_visualizacion = ttkb.Frame(self.notebook, padding=20, bootstyle="info")

        self.notebook.add(frame_visualizacion, text="Visualización de Datos")

        ttk.Label(frame_visualizacion, text="Nombre del empleado:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_nombre_grafico = ttk.Entry(frame_visualizacion, font=('Arial', 10))
        self.entry_nombre_grafico.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Button(frame_visualizacion, text="Mostrar Gráfico", bootstyle="success", command=self.mostrar_grafico).grid(row=1, columnspan=2, pady=10)

        self.datos_label = ttk.Label(frame_visualizacion, text="", font=('Arial', 10), justify=tk.LEFT)
        self.datos_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def crear_pestana_gestion_registros(self):
        """Crear la pestaña de gestión de registros (ver, eliminar)."""
        frame_gestion = ttkb.Frame(self.notebook, padding=20, bootstyle="info")

        self.notebook.add(frame_gestion, text="Gestión de Registros")

        self.listbox_empleados = tk.Listbox(frame_gestion, height=10, width=50, font=('Arial', 10))
        self.listbox_empleados.grid(row=0, column=0, padx=10, pady=5)

        self.actualizar_listbox()

        ttk.Button(frame_gestion, text="Eliminar Registro", bootstyle="danger", command=self.eliminar_registro).grid(row=1, column=0, pady=10)

    def actualizar_listbox(self):
        """Actualizar el contenido del Listbox con los empleados registrados."""
        self.listbox_empleados.delete(0, tk.END)
        for nombre in self.empleados:
            self.listbox_empleados.insert(tk.END, nombre)

    def guardar_registro(self):
        """Guardar el registro de un nuevo empleado."""
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        edad = self.entry_edad.get()
        telefono = self.entry_telefono.get()
        email = self.entry_email.get()

        if nombre and apellido and edad.isdigit() and telefono.isdigit() and email:
            if nombre in self.empleados:
                messagebox.showwarning("Error", "El empleado ya está registrado.")
            else:
                self.empleados[nombre] = {
                    "apellido": apellido,
                    "edad": int(edad),
                    "telefono": telefono,
                    "email": email,
                    "rueda": {campo[1]: 0 for campo in self.campos}
                }
                self.guardar_datos()
                messagebox.showinfo("Registro Exitoso", "Empleado registrado correctamente.")
                self.entry_nombre.delete(0, tk.END)
                self.entry_apellido.delete(0, tk.END)
                self.entry_edad.delete(0, tk.END)
                self.entry_telefono.delete(0, tk.END)
                self.entry_email.delete(0, tk.END)
                self.actualizar_listbox()
        else:
            messagebox.showwarning("Error", "Por favor, completa todos los campos correctamente.")

    def eliminar_registro(self):
        """Eliminar un registro de empleado."""
        seleccionado = self.listbox_empleados.curselection()

        if seleccionado:
            nombre = self.listbox_empleados.get(seleccionado)

            if messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de eliminar el empleado {nombre}?"):
                del self.empleados[nombre]
                self.guardar_datos()
                self.actualizar_listbox()
                messagebox.showinfo("Eliminado", f"Empleado {nombre} eliminado correctamente.")
        else:
            messagebox.showwarning("Error", "Selecciona un empleado para eliminar.")

    def guardar_respuestas(self):
        """Guardar las respuestas de la Rueda de la Vida."""
        nombre = self.entry_nombre_respuestas.get()
        try:
            respuestas = {
                campo[1]: int(getattr(self, campo[1]).get())
                for campo in self.campos
            }

            if not all(1 <= valor <= 10 for valor in respuestas.values()):
                messagebox.showwarning("Error", "Las respuestas deben estar entre 1 y 10.")
                return

            if nombre in self.empleados:
                self.empleados[nombre]["rueda"] = respuestas
                self.guardar_datos()
                messagebox.showinfo("Respuestas Guardadas", "Respuestas guardadas correctamente.")
            else:
                messagebox.showwarning("Error", "Empleado no encontrado.")
        except ValueError:
            messagebox.showwarning("Error", "Por favor, ingresa respuestas válidas.")

    def mostrar_grafico(self):
        """Mostrar el gráfico de la Rueda de la Vida del empleado seleccionado."""
        nombre = self.entry_nombre_grafico.get()

        if nombre in self.empleados:
            respuestas = self.empleados[nombre]["rueda"]
            etiquetas = [campo[0] for campo in self.campos]
            valores = [respuestas[campo[1]] for campo in self.campos]

            # Crear gráfico de radar
            fig, ax = plt.subplots(figsize=(6, 6), dpi=100, subplot_kw=dict(polar=True))

            angles = [n / float(len(valores)) * 2 * 3.1416 for n in range(len(valores))]
            valores += valores[:1]
            angles += angles[:1]
            ax.set_theta_offset(3.1416 / 2)
            ax.set_theta_direction(-1)

            ax.plot(angles, valores, linewidth=1, linestyle='solid', label=nombre)
            ax.fill(angles, valores, alpha=0.4)

            ax.set_yticklabels([])
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(etiquetas)

            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas.get_tk_widget().pack()
            canvas.draw()
        else:
            messagebox.showwarning("Error", "Empleado no encontrado.")

if __name__ == "__main__":
    root = ttkb.Window(title="Gestión de Empleados", size=(800, 600))
    app = Aplicacion(root)
    root.mainloop()