# Importaciones:
import ttkbootstrap as tb
from tkinter import Toplevel
from tkinter import Label

def ventana_modificar_producto(parent):
    """Interfaz para la modificacion de un producto"""

    # Importaciones perezosas
    from logica.logica_productos.centrar_ventana_modificar_producto import centrar_ventana_modificar_producto
    from logica.logica_productos.guardar_producto import guardar_producto
    from logica.logica_productos.llenar_entrys_modificar_productos import llenar_entrys_modificar_producto

    parent.producto_seleccionado = parent.tree_lista_productos.focus()
    parent.valor_producto_seleccionado = parent.tree_lista_productos.item(parent.producto_seleccionado, 'values')

    if parent.valor_producto_seleccionado != '':
        # Configuracion de la ventana
        parent.frame_modificar_producto = Toplevel(master = parent)
        parent.frame_modificar_producto.title('Modificar producto')
        centrar_ventana_modificar_producto(parent.frame_modificar_producto, 400, 450)
        parent.frame_modificar_producto.grab_set()

        lblframe_modificar_producto = tb.LabelFrame(master = parent.frame_modificar_producto, text = 'Modificar Producto')
        lblframe_modificar_producto.pack(padx = 15, pady = 15)

        # Codigo
        lbl_codigo_modificar_producto = Label(master = lblframe_modificar_producto, text = 'Codigo')
        lbl_codigo_modificar_producto.grid(row = 0, column = 0, padx = 10, pady = 10)
        parent.ent_codigo_modificar_producto = tb.Entry(master = lblframe_modificar_producto, width = 40)
        parent.ent_codigo_modificar_producto.grid(row = 0, column = 1, padx = 10, pady = 10)

        # Descripcion
        lbl_nombre_modificar_producto = Label(master = lblframe_modificar_producto, text = 'Descripcion')
        lbl_nombre_modificar_producto.grid(row = 1, column = 0, padx = 10, pady = 10)
        parent.ent_nombre_modificar_producto = tb.Entry(master = lblframe_modificar_producto, width = 40)
        parent.ent_nombre_modificar_producto.grid(row = 1, column = 1, padx = 10, pady = 10)

        # Laboratorio
        lbl_laboratorio_modificar_producto = Label(master = lblframe_modificar_producto, text = 'Laboratorio')
        lbl_laboratorio_modificar_producto.grid(row = 2, column = 0, padx = 10, pady = 10)
        parent.ent_laboratorio_modificar_producto = tb.Entry(master = lblframe_modificar_producto, width = 40)
        parent.ent_laboratorio_modificar_producto.grid(row = 2, column = 1, padx = 10, pady = 10)

        # Costo
        lbl_costo_modificar_producto = Label(master = lblframe_modificar_producto, text = 'Costo')
        lbl_costo_modificar_producto.grid(row = 3, column = 0, padx = 10, pady = 10)
        parent.ent_costo_modificar_producto = tb.Entry(master = lblframe_modificar_producto, width = 40)
        parent.ent_costo_modificar_producto.grid(row = 3, column = 1, padx = 10, pady = 10)

        # Precio
        lbl_precio_modificar_producto = Label(master = lblframe_modificar_producto, text = 'Precio')
        lbl_precio_modificar_producto.grid(row = 4, column = 0, padx = 10, pady = 10)
        parent.ent_precio_modificar_producto = tb.Entry(master = lblframe_modificar_producto, width = 40)
        parent.ent_precio_modificar_producto.grid(row = 4, column = 1, padx = 10, pady = 10)

        # Stock
        lbl_stock_modificar_producto = Label(master = lblframe_modificar_producto, text = 'Stock')
        lbl_stock_modificar_producto.grid(row = 5, column = 0, padx = 10, pady = 10)
        parent.ent_stock_modificar_producto = tb.Entry(master = lblframe_modificar_producto, width = 40)
        parent.ent_stock_modificar_producto.grid(row = 5, column = 1, padx = 10, pady = 10)

        # Minimo
        lbl_minimo_modificar_producto = Label(master = lblframe_modificar_producto, text = 'Minimo')
        lbl_minimo_modificar_producto.grid(row = 6, column = 0, padx = 10, pady = 10)
        parent.ent_minimo_modificar_producto = tb.Entry(master = lblframe_modificar_producto, width = 40)
        parent.ent_minimo_modificar_producto.grid(row = 6, column = 1, padx = 10, pady = 10)

        # Configuracion del boton para guardar producto
        btn_guardar_producto = tb.Button(master = lblframe_modificar_producto, text = 'Modificar', width = 38,
                                        bootstyle = 'warning')
        btn_guardar_producto.grid(row = 7, column = 1, padx = 10, pady = 10)

        llenar_entrys_modificar_producto(parent)
        # Mejorar experiencia del usuario
        parent.ent_nombre_modificar_producto.focus()
        # Vincular Enter para avanzar entre campos
        parent.ent_nombre_modificar_producto.bind("<Return>", lambda e: parent.ent_laboratorio_modificar_producto.focus())
        parent.ent_laboratorio_modificar_producto.bind("<Return>", lambda e: parent.ent_costo_modificar_producto.focus())
        parent.ent_costo_modificar_producto.bind("<Return>", lambda e: parent.ent_precio_modificar_producto.focus())
        parent.ent_precio_modificar_producto.bind("<Return>", lambda e: parent.ent_stock_modificar_producto.focus())
        parent.ent_stock_modificar_producto.bind("<Return>", lambda e: parent.ent_minimo_modificar_producto.focus())
        parent.ent_minimo_modificar_producto.bind("<Return>", lambda e: guardar_producto(parent))

    