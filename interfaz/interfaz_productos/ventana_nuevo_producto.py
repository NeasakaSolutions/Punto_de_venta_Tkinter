# Importaciones:
import ttkbootstrap as tb
from tkinter import Toplevel
from tkinter import Label

def ventana_nuevo_producto(parent):
    """Interfaz para la creacion de un nuevo producto"""

    # Importaciones perezosas
    from logica.logica_productos.centrar_ventana_nuevo_producto import centrar_ventana_nuevo_producto

    # Configuracion de la ventana
    parent.frame_nuevo_producto = Toplevel(master = parent)
    parent.frame_nuevo_producto.title('Nuevo Producto')
    centrar_ventana_nuevo_producto(parent.frame_nuevo_producto, 400, 450)
    parent.frame_nuevo_producto.grab_set()

    lblframe_nuevo_producto = tb.LabelFrame(master = parent.frame_nuevo_producto, text = 'Nuevo Producto')
    lblframe_nuevo_producto.pack(padx = 15, pady = 15)

    # Codigo
    lbl_codigo_nuevo_producto = Label(master = lblframe_nuevo_producto, text = 'Codigo')
    lbl_codigo_nuevo_producto.grid(row = 0, column = 0, padx = 10, pady = 10)
    parent.ent_codigo_nuevo_producto = tb.Entry(master = lblframe_nuevo_producto, width = 40)
    parent.ent_codigo_nuevo_producto.grid(row = 0, column = 1, padx = 10, pady = 10)

    # Descripcion
    lbl_nombre_nuevo_producto = Label(master = lblframe_nuevo_producto, text = 'Descripcion')
    lbl_nombre_nuevo_producto.grid(row = 1, column = 0, padx = 10, pady = 10)
    parent.ent_nombre_nuevo_producto = tb.Entry(master = lblframe_nuevo_producto, width = 40)
    parent.ent_nombre_nuevo_producto.grid(row = 1, column = 1, padx = 10, pady = 10)

    # Laboratorio
    lbl_laboratorio_nuevo_producto = Label(master = lblframe_nuevo_producto, text = 'Laboratorio')
    lbl_laboratorio_nuevo_producto.grid(row = 2, column = 0, padx = 10, pady = 10)
    parent.ent_laboratorio_nuevo_producto = tb.Entry(master = lblframe_nuevo_producto, width = 40)
    parent.ent_laboratorio_nuevo_producto.grid(row = 2, column = 1, padx = 10, pady = 10)

    # Costo
    lbl_costo_nuevo_producto = Label(master = lblframe_nuevo_producto, text = 'Costo')
    lbl_costo_nuevo_producto.grid(row = 3, column = 0, padx = 10, pady = 10)
    parent.ent_costo_nuevo_producto = tb.Entry(master = lblframe_nuevo_producto, width = 40)
    parent.ent_costo_nuevo_producto.grid(row = 3, column = 1, padx = 10, pady = 10)

    # Precio
    lbl_precio_nuevo_producto = Label(master = lblframe_nuevo_producto, text = 'Precio')
    lbl_precio_nuevo_producto.grid(row = 4, column = 0, padx = 10, pady = 10)
    parent.ent_precio_nuevo_producto = tb.Entry(master = lblframe_nuevo_producto, width = 40)
    parent.ent_precio_nuevo_producto.grid(row = 4, column = 1, padx = 10, pady = 10)

    # Stock
    lbl_stock_nuevo_producto = Label(master = lblframe_nuevo_producto, text = 'Stock')
    lbl_stock_nuevo_producto.grid(row = 5, column = 0, padx = 10, pady = 10)
    parent.ent_stock_nuevo_producto = tb.Entry(master = lblframe_nuevo_producto, width = 40)
    parent.ent_stock_nuevo_producto.grid(row = 5, column = 1, padx = 10, pady = 10)

    # Minimo
    lbl_minimo_nuevo_producto = Label(master = lblframe_nuevo_producto, text = 'Minimo')
    lbl_minimo_nuevo_producto.grid(row = 6, column = 0, padx = 10, pady = 10)
    parent.ent_minimo_nuevo_producto = tb.Entry(master = lblframe_nuevo_producto, width = 40)
    parent.ent_minimo_nuevo_producto.grid(row = 6, column = 1, padx = 10, pady = 10)

    # Configuracion del boton para guardar producto
    btn_guardar_producto = tb.Button(master = lblframe_nuevo_producto, text = 'Guardar', width = 38,
                                    bootstyle = 'success')
    btn_guardar_producto.grid(row = 7, column = 1, padx = 10, pady = 10)

    # Mejorar experiencia del usuario
    parent.ent_nombre_nuevo_producto.focus()
    # Vincular Enter para avanzar entre campos
    parent.ent_nombre_nuevo_producto.bind("<Return>", lambda e: parent.ent_laboratorio_nuevo_producto.focus())
    parent.ent_laboratorio_nuevo_producto.bind("<Return>", lambda e: parent.ent_costo_nuevo_producto.focus())
    parent.ent_costo_nuevo_producto.bind("<Return>", lambda e: parent.ent_precio_nuevo_producto.focus())
    parent.ent_precio_nuevo_producto.bind("<Return>", lambda e: parent.ent_stock_nuevo_producto.focus())
    parent.ent_stock_nuevo_producto.bind("<Return>", lambda e: parent.ent_minimo_nuevo_producto.focus())
    # parent.ent_minimo_nuevo_producto.bind("<Return>", lambda e: guardar_producto(parent))

    