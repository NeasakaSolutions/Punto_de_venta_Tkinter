# Importaciones:
from tkinter import messagebox
from base_datos.conexion import conectar

def agregar_producto_detalle_venta(parent):
    '''Configuracion para el guardado de productos en detalle de venta'''

    # Importaciones perezosas
    

    try:
        # conexion a la bd
        mi_conexion = conectar()
        # Crear el cursor
        mi_cursor = mi_conexion.cursor()

        # Crear la cosulta
        mi_cursor.execute("INSERT INTO DetalleVentaT VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                          (parent.datos_guardar_producto_detalle_venta))

        # Aplicar cambios
        mi_conexion.commit()

        # Avisar que se guardo
        messagebox.showinfo('Agregando productos detalle venta', 'Registro agregado correctamente.')

        # Cerrar conexion
        mi_conexion.close()
    except:
         messagebox.showerror('Agregando productos detalle venta', 'Ocurrio un error.')