# Importaciones
from tkinter import messagebox
from base_datos.conexion import conectar


def modificar_producto(parent):
    """Configuracion para la modificacion de los productos """


    if (parent.ent_codigo_modificar_producto.get() == '' or parent.ent_nombre_modificar_producto.get() == ''
        or parent.ent_laboratorio_modificar_producto.get() == '' or parent.ent_costo_modificar_producto.get() == ''
        or parent.ent_precio_modificar_producto.get() == '' or parent.ent_stock_modificar_producto.get() == ''
        or parent.ent_minimo_modificar_producto.get() == ''):
            messagebox.showerror('Modificando producto', 'Favor de llenar todos los campos.')
            return
    
    try:
        # conexion a la bd
        mi_conexion = conectar()
        # Crear el cursor
        mi_cursor = mi_conexion.cursor()

        modificar_datos_producto = (parent.ent_nombre_modificar_producto.get(),
        parent.ent_laboratorio_modificar_producto.get(), parent.ent_costo_modificar_producto.get(),
        parent.ent_precio_modificar_producto.get(), parent.ent_stock_modificar_producto.get(),
        parent.ent_minimo_modificar_producto.get())

        # Crear la cosulta
        mi_cursor.execute("UPDATE Productos SET Nombre = ?, Laboratorio = ?, Costo = ?, " \
        "Precio = ?, Stock = ?, Minimo = ? WHERE Codigo = " 
        + parent.ent_codigo_modificar_producto.get(), (modificar_datos_producto))

        # Aplicar cambios
        mi_conexion.commit()

        # Avisar que se guardo
        messagebox.showinfo('Modificando Producto', 'Registro modificado correctamente.')

        parent.valor_producto_seleccionado = parent.tree_lista_productos.item(parent.producto_seleccionado,
                                            text = '', values = (parent.ent_codigo_modificar_producto.get(), 
                                            parent.ent_nombre_modificar_producto.get(),
                                            parent.ent_laboratorio_modificar_producto.get(), 
                                            parent.ent_costo_modificar_producto.get(),
                                            parent.ent_precio_modificar_producto.get(), 
                                            parent.ent_stock_modificar_producto.get(),
                                            parent.ent_minimo_modificar_producto.get()))
        
        parent.frame_modificar_producto.destroy()

        # Cerrar conexion
        mi_conexion.close()
    except:
         messagebox.showerror('Modificando producto', 'Ocurrio un error.')

