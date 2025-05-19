# Importaciones:
from tkinter import NORMAL
from tkinter import messagebox
from base_datos.conexion import conectar

def correlativo_productos(parent):
    """Funcion que ordena las id de los productos"""

    try:
        # conexion a la bd
        mi_conexion = conectar()
        # Crear el cursor
        mi_cursor = mi_conexion.cursor()

        # Crear la cosulta
        mi_cursor.execute("SELECT MAX(Codigo) FROM Productos")
        correlativo_productos = mi_cursor.fetchone()

        for datos in correlativo_productos:
            if datos == None:
                parent.nuevo_correlativo_producto = (int(1))
                parent.ent_codigo_nuevo_producto.config(state = NORMAL)
                parent.ent_codigo_nuevo_producto.insert(0, parent.nuevo_correlativo_producto)
                parent.ent_codigo_nuevo_producto.config(state = 'readonly')
            else:
                parent.nuevo_correlativo_producto = (int(datos) + 1)
                parent.ent_codigo_nuevo_producto.config(state = NORMAL)
                parent.ent_codigo_nuevo_producto.insert(0, parent.nuevo_correlativo_producto)
                parent.ent_codigo_nuevo_producto.config(state = 'readonly')

        # Aplicar cambios
        mi_conexion.commit()
        # Cerrar conexion
        mi_conexion.close()

    except:
        messagebox.showerror('Correlativo productos', 'Ocurrio un error')

