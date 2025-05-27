# Importaciones
from base_datos.conexion import conectar
from tkinter import messagebox

def mostrar_productos_detalle_venta(parent):
    """ Muestra los productos de una venta en detalle. """

    try:
        # conexion a la bd
        mi_conexion = conectar()
        # Crear el cursor
        mi_cursor = mi_conexion.cursor()
        
        # Limpiar el treeview
        registro = parent.tree_detalle_venta.get_children()
        for elementos in registro:
            parent.tree_detalle_venta.delete(elementos)

        # Crear la cosulta
        mi_cursor.execute("SELECT * FROM DetalleVentaT")
        datos_productos_detalle_venta = mi_cursor.fetchall()

        # insertar las filas en el treeview
        for fila in datos_productos_detalle_venta:
            # Calcular el subtotal y la existencia
            subtotal = float(fila[4] * fila[5])
            existencia = int(fila[6] - fila[5])

            parent.tree_detalle_venta.insert('', 0, text = fila[0], values = (fila[0], fila[1], fila[2], 
                                                fila[3], fila[4], fila[5], fila[6], fila[7], 
                                                subtotal, existencia))

        # Aplicar cambios
        mi_conexion.commit()
        # Cerrar conexion
        mi_conexion.close()
    
    except:
        messagebox.showerror('Buscar producto detalle venta', 'Ocurrio un error')