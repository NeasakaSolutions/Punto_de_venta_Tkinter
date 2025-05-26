# Importaciones:
#from tkinter import messagebox
from tkinter import StringVar
from tkinter import Radiobutton
from base_datos.conexion import conectar

def buscar_productos_detalle_venta(parent, event=None):
    # conexión a la bd
    mi_conexion = conectar()
    mi_cursor = mi_conexion.cursor()
    
    # Limpiar el scrollframe
    for wid in parent.frame_busqueda_detalle_venta.winfo_children():
        wid.destroy()

    # Crear la consulta
    mi_cursor.execute("SELECT * FROM Productos WHERE Nombre LIKE ?", 
                      (parent.ent_buscar_detalle_venta.get() + '%',))
    datos_productos_detalle_venta = mi_cursor.fetchall()

    codigo_busqueda_detalle_venta = StringVar()
    contador = 0
    filas = 2

    # Configurar columnas para que se expandan
    for col in range(filas):
        parent.frame_busqueda_detalle_venta.grid_columnconfigure(col, weight=1)

    # Insertar las filas en el scrollframe
    for row in datos_productos_detalle_venta:
        radbutton = Radiobutton(master=parent.frame_busqueda_detalle_venta,
                               text=row[1] + '\n' + row[2] + '\n' + str(row[4]),
                               value=row[0], indicator=0, width=20, height=5)
        radbutton.grid(row=contador // filas, column=contador % filas, padx=5, pady=5, sticky="nsew")
        contador += 1

    mi_conexion.commit()
    mi_conexion.close()
