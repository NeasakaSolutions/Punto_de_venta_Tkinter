from tkinter import messagebox
from base_datos.conexion import conectar
from logica.logica_ventas.mostrar_productos_detalle_venta import mostrar_productos_detalle_venta

def agregar_producto_detalle_venta(parent):
    '''Configuración para el guardado de productos en detalle de venta'''

    try:
        mi_conexion = conectar()
        mi_cursor = mi_conexion.cursor()

        codigo = parent.datos_guardar_producto_detalle_venta[1]

        mi_cursor.execute("SELECT COUNT(*) FROM DetalleVentaT WHERE Codigo = ?", (codigo,))
        existe = mi_cursor.fetchone()[0]

        if existe == 0:
            mi_cursor.execute(
                "INSERT INTO DetalleVentaT VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                parent.datos_guardar_producto_detalle_venta
            )
            mi_conexion.commit()
            messagebox.showinfo('Agregando productos detalle venta', 'Registro agregado correctamente.')
        else:
            messagebox.showinfo('Agregando productos detalle venta', 'Este producto ya fue agregado.')

        mostrar_productos_detalle_venta(parent)

        # Limpiar el campo de búsqueda y la variable para el siguiente producto
        parent.ent_buscar_codigo_detalle_venta.delete(0, 'end')
        parent.datos_guardar_producto_detalle_venta = None

        mi_conexion.close()

    except Exception as e:
        messagebox.showerror('Agregando productos detalle venta', f'Ocurrió un error.')