# Importaciones:
from base_datos.conexion import conectar

def producto_seleccionado_detalle_venta(parent):
    """Funcion que muestra los productos atravez de consultas"""

    # Importaciones perezosas
    from logica.logica_ventas.agregar_producto_detalle_venta import agregar_producto_detalle_venta
    from logica.logica_ventas.mostrar_productos_detalle_venta import mostrar_productos_detalle_venta

    # conexion a la bd
    mi_conexion = conectar()
    # Crear el cursor
    mi_cursor = mi_conexion.cursor()
        
    # Crear la cosulta
    mi_cursor.execute("SELECT * FROM Productos WHERE Codigo = " +
                    parent.ent_buscar_codigo_detalle_venta.get())
    datos_producto_seleccionado = mi_cursor.fetchall()

    # condicion para verificar si se encontro el producto
    if datos_producto_seleccionado != None:
        # guardar las filas en una variable
        for fila in datos_producto_seleccionado:
            parent.datos_guardar_producto_detalle_venta = ('1', fila[0], fila[1], fila[3],
                                                            fila[4], '1', fila[5], '0')
            
    # Llamar a la funcion para agregar el producto al detalle de venta
    agregar_producto_detalle_venta(parent)
    mostrar_productos_detalle_venta(parent)

    # Aplicar cambios
    mi_conexion.commit()
    # Cerrar conexion
    mi_conexion.close()


