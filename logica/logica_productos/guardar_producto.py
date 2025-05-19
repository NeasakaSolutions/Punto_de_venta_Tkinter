# Importaciones
from tkinter import messagebox
from base_datos.conexion import conectar

def guardar_producto(parent):
    """Configuracion para el guardado de productos """

    # Importaciones perezosas
    from logica.logica_productos.buscar_producto import buscar_producto

    if (parent.ent_codigo_nuevo_producto.get() == '' or parent.ent_nombre_nuevo_producto.get() == ''
        or parent.ent_laboratorio_nuevo_producto.get() == '' or parent.ent_costo_nuevo_producto.get() == ''
        or parent.ent_precio_nuevo_producto.get() == '' or parent.ent_stock_nuevo_producto.get() == ''
        or parent.ent_minimo_nuevo_producto.get() == ''):
            messagebox.showerror('Guardando producto', 'Favor de llenar todos los campos.')
            return
    
    try:
        # conexion a la bd
        mi_conexion = conectar()
        # Crear el cursor
        mi_cursor = mi_conexion.cursor()

        guardar_datos_producto = (parent.ent_codigo_nuevo_producto.get(), parent.ent_nombre_nuevo_producto.get(),
        parent.ent_laboratorio_nuevo_producto.get(), parent.ent_costo_nuevo_producto.get(),
        parent.ent_precio_nuevo_producto.get(), parent.ent_stock_nuevo_producto.get(),
        parent.ent_minimo_nuevo_producto.get())

        # Crear la cosulta
        mi_cursor.execute("INSERT INTO Productos VALUES (?, ?, ?, ?, ?, ?, ?)", (guardar_datos_producto))

        # Aplicar cambios
        mi_conexion.commit()

        # Avisar que se guardo
        messagebox.showinfo('Guardando producto', 'Registro guardado correctamente.')
        parent.frame_nuevo_producto.destroy()
        
        buscar_producto(parent, event = None)

        # Cerrar conexion
        mi_conexion.close()
    except:
         messagebox.showerror('Guardando producto', 'Ocurrio un error.')




