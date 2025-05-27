# Importaciones:
from tkinter import messagebox
from base_datos.conexion import conectar

def producto_seleccionado_detalle_venta(parent):
    """Funcion que muestra los productos atravez de consultas"""

    # conexion a la bd
    mi_conexion = conectar()
    # Crear el cursor
    mi_cursor = mi_conexion.cursor()
        
    # Crear la cosulta
    mi_cursor.execute("SELECT * FROM Productos WHERE Codigo = " +
                    parent.ent_buscar_codigo_detalle_venta.get())
    datos_producto_seleccionado = mi_cursor.fetchall()
    print(datos_producto_seleccionado)

    # condicion para verificar si se encontro el producto
    if datos_producto_seleccionado != None:
        # guardar las filas en una variable
        for fila in datos_producto_seleccionado:
            parent.datos_guardar_producto_detalle_venta = ('1', fila[0], fila[1], fila[3],
                                                            fila[4], '1', fila[5], '0')

    # Aplicar cambios
    mi_conexion.commit()
    # Cerrar conexion
    mi_conexion.close()


