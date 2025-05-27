# Importaciones:
import ttkbootstrap as tb
from tkinter import Frame
from tkinter import W
from tkinter import NSEW
from tkinter import CENTER

def ventana_detalle_venta(parent):
    """Crea una ventana para mostrar detalles de las ventas."""

    # Importaciones perezosas
    from interfaz.interfaz_detalle_de_venta.busqueda_descripcion import busqueda_descripcion
    from interfaz.interfaz_detalle_de_venta.busqueda_codigo import busqueda_codigo
    from interfaz.interfaz_detalle_de_venta.ventana_busqueda_detalle_venta import ventana_busqueda_detalle_venta
    from logica.general.borrar_frames import borrar_frames
    from logica.logica_ventas.buscar_producto_detalle_venta import buscar_productos_detalle_venta
    from logica.logica_ventas.producto_seleccionado_detalle_venta import producto_seleccionado_detalle_venta

    # Crear un marco para la ventana
    borrar_frames(parent)
    parent.frame_detalle_venta = Frame(master = parent.frame_center)
    parent.frame_detalle_venta.grid(row = 0, column = 1, sticky = "NSEW")

    # Configurar el diseño de la ventana
    lblframe_botones_detalle_venta = tb.LabelFrame(master = parent.frame_detalle_venta)
    lblframe_botones_detalle_venta.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "NSEW")

    # Botón para detalles de venta
    btn_detalle = tb.Button(master = lblframe_botones_detalle_venta, text = "Detalle", 
                                         width = 12, bootstyle = "info", 
                                         command = lambda: producto_seleccionado_detalle_venta(parent))
    btn_detalle.grid(row = 0, column = 0, padx = 5, pady = 10)

    # Botón para cantidades de productos
    btn_cantidad = tb.Button(master = lblframe_botones_detalle_venta, text = "Cantidad", 
                                         width = 12, bootstyle = "primary")
    btn_cantidad.grid(row = 0, column = 1, padx = 5, pady = 10)

    # Botón para borrar
    btn_borrar = tb.Button(master = lblframe_botones_detalle_venta, text = "Borrar", 
                                         width = 12, bootstyle = "danger")
    btn_borrar.grid(row = 0, column = 2, padx = 4, pady = 10)

    # Botón para dedscuento en los productos
    btn_descuento = tb.Button(master = lblframe_botones_detalle_venta, text = "Descuento", 
                                         width = 12, bootstyle = "warning")
    btn_descuento.grid(row = 0, column = 3, padx = 4, pady = 10)

    # Botón para cobrar
    btn_cobrar = tb.Button(master = lblframe_botones_detalle_venta, text = "Cobrar", 
                                         width = 12, bootstyle = "success")
    btn_cobrar.grid(row = 0, column = 4, padx = 5, pady = 10)

    # Botón para credito
    btn_credito = tb.Button(master = lblframe_botones_detalle_venta, text = "Credito", 
                                         width = 12, bootstyle = "warning")
    btn_credito.grid(row = 0, column = 5, padx = 5, pady = 10)

    # Llamado a la barra de busqueda
    busqueda_codigo(parent)
    busqueda_descripcion(parent)

    # Botón para buscar detalles de venta
    lblframe_tree_lista_detalle_venta = tb.LabelFrame(master = parent.frame_detalle_venta)
    lblframe_tree_lista_detalle_venta.grid(row = 2, column = 0, sticky = "NSEW",)

    # Crear columnas:
    columnas = ("no", "codigo", "descripcion", "costo", "precio", "cantidad", "stock", "descuento", 
                "subtotal", "existencia")

    # Crear el Treeview para mostrar la lista de usuarios
    parent.tree_detalle_venta = tb.Treeview(master = lblframe_tree_lista_detalle_venta, height = 17, 
                                              columns = columnas ,show = "headings", 
                                              bootstyle = "success")
    
    parent.tree_detalle_venta.grid(row = 0, column = 0, padx = 10, pady = 10)

    # Crear las cabeceras
    parent.tree_detalle_venta.heading('no', text = 'No', anchor = W)
    parent.tree_detalle_venta.heading('codigo', text = 'Codigo', anchor = W)
    parent.tree_detalle_venta.heading('descripcion', text = 'Descripcion', anchor = W)
    parent.tree_detalle_venta.heading('costo', text = 'Costo', anchor = W)
    parent.tree_detalle_venta.heading('precio', text = 'Precio', anchor = W)
    parent.tree_detalle_venta.heading('cantidad', text = 'Cantidad', anchor = W)
    parent.tree_detalle_venta.heading('stock', text = 'Stock', anchor = W)
    parent.tree_detalle_venta.heading('descuento', text = 'Descuento', anchor = W)
    parent.tree_detalle_venta.heading('subtotal', text = 'Subtotal', anchor = W)
    parent.tree_detalle_venta.heading('existencia', text = 'Existencia', anchor = W)

    # Configurar las columnas a mostrar:
    parent.tree_detalle_venta['displaycolumns'] = ('codigo', 'descripcion', 'precio', 'cantidad', 
                                                     'subtotal', 'existencia')

    # Tamanio de las columnas
    parent.tree_detalle_venta.column('no', width = 0)
    parent.tree_detalle_venta.column('codigo', width = 55)
    parent.tree_detalle_venta.column('descripcion', width = 240)
    parent.tree_detalle_venta.column('costo', width = 100)
    parent.tree_detalle_venta.column('precio', width = 100)
    parent.tree_detalle_venta.column('cantidad', width = 75)
    parent.tree_detalle_venta.column('stock', width = 75)
    parent.tree_detalle_venta.column('descuento', width = 100)
    parent.tree_detalle_venta.column('subtotal', width = 100)
    parent.tree_detalle_venta.column('existencia', width = 80)

    # Crear el scrollbar
    tree_scroll = tb.Scrollbar(master = lblframe_tree_lista_detalle_venta, bootstyle = "success-round")
    tree_scroll.grid(row = 0, column = 1, padx = 5, pady = 10)

    # Configurar el scrollbar
    tree_scroll.config(command = parent.tree_detalle_venta.yview)

    lblframe_total_detalle_venta = tb.LabelFrame(master = parent.frame_detalle_venta)
    lblframe_total_detalle_venta.grid(row = 3, column = 0, sticky = NSEW)

    parent.ent_total_detalle_venta = tb.Entry(master = lblframe_total_detalle_venta, width = 39,
                                              font = ('calibri', 24), justify = CENTER)
    parent.ent_total_detalle_venta.grid(row = 0, column = 0)

    #buscar_producto(parent, None)
    parent.ent_buscar_detalle_venta.focus()
    ventana_busqueda_detalle_venta(parent)
    buscar_productos_detalle_venta(parent)






