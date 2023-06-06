import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import statistics
import matplotlib.pyplot as plt
import numpy as np

class AplicativoEstadistico:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo Estadístico Básico")

        # Crear el contenedor principal
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.grid()

        # Crear etiqueta de título
        self.title_label = ttk.Label(self.main_frame, text="Aplicativo Estadístico Básico", font=("Helvetica", 18))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Crear botones para acceder a las diferentes opciones
        self.button_tendencia_central = ttk.Button(self.main_frame, text="Medidas de Tendencia Central",
                                                   command=self.calcular_tendencia_central)
        self.button_tendencia_central.grid(row=1, column=0, pady=10)

        self.button_posicion = ttk.Button(self.main_frame, text="Medidas de Posición",
                                          command=self.calcular_posicion)
        self.button_posicion.grid(row=2, column=0, pady=10)

        self.button_dispercion = ttk.Button(self.main_frame, text="Medidas de Dispersión",
                                            command=self.calcular_dispercion)
        self.button_dispercion.grid(row=3, column=0, pady=10)

        self.button_graficar = ttk.Button(self.main_frame, text="Graficar Datos",
                                          command=self.graficar_datos)
        self.button_graficar.grid(row=4, column=0, pady=10)

        self.button_ingresar_datos = ttk.Button(self.main_frame, text="Ingresar Datos",
                                                command=self.ingresar_datos)
        self.button_ingresar_datos.grid(row=5, column=0, pady=10)

        self.button_salir = ttk.Button(self.main_frame, text="Salir", command=root.quit)
        self.button_salir.grid(row=6, column=0, pady=10)

        self.data = []

    def ingresar_datos(self):
        data_str = simpledialog.askstring("Ingresar Datos", "Ingrese los datos separados por comas:")
        if data_str is not None:
            try:
                self.data = [float(x.strip()) for x in data_str.split(",")]
                messagebox.showinfo("Ingresar Datos", "Datos ingresados correctamente.")
            except ValueError:
                messagebox.showerror("Error", "Formato de datos inválido. Ingrese números separados por comas.")

    def calcular_tendencia_central(self):
        if len(self.data) == 0:
            messagebox.showerror("Error", "No se han ingresado datos.")
            return

        moda = statistics.mode(self.data)
        mediana = statistics.median(self.data)
        media = statistics.mean(self.data)

        messagebox.showinfo("Medidas de Tendencia Central",
                            f"Moda: {moda}\nMediana: {mediana}\nMedia: {media}")

    

    def calcular_posicion(self):
        if len(self.data) == 0:
            messagebox.showerror("Error", "No se han ingresado datos.")
            return

        posicion_str = simpledialog.askstring("Posición", "Ingrese la posición (valor entre 0 y 1):")
        if posicion_str is None:
            return

        try:
            posicion = float(posicion_str)
            if 0 <= posicion <= 1:
                valor = np.percentile(self.data, posicion * 100)
                messagebox.showinfo("Medidas de Posición", f"Valor en la posición {posicion}: {valor}")
            else:
                messagebox.showerror("Error", "Posición inválida. Debe ser un valor entre 0 y 1.")
        except ValueError:
            messagebox.showerror("Error", "Posición inválida. Debe ser un número entre 0 y 1.")


    def calcular_dispercion(self):
        if len(self.data) == 0:
            messagebox.showerror("Error", "No se han ingresado datos.")
            return

        varianza = statistics.variance(self.data)
        desviacion_estandar = statistics.stdev(self.data)

        messagebox.showinfo("Medidas de Dispersión",
                            f"Varianza: {varianza}\nDesviación Estándar: {desviacion_estandar}")

    def graficar_datos(self):
        if len(self.data) == 0:
            messagebox.showerror("Error", "No se han ingresado datos.")
            return

        indices = list(range(1, len(self.data) + 1))

        plt.plot(indices, self.data, marker='o', linestyle='-')
        plt.xlabel("Orden")
        plt.ylabel("Valor")
        plt.title("Valores en función del Orden")
        plt.show()


# Crear la ventana principal
root = tk.Tk()
app = AplicativoEstadistico(root)
root.mainloop()
