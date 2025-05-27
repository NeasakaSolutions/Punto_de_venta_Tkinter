# Importaciones
import ttkbootstrap as tb
from tkinter import NSEW


def busqueda_codigo(parent):
    """Funcion para la configuracion de la barra de busqueda del codigo"""

    # Importaciones perezosas
    from interfaz.interfaz_detalle_de_venta.busqueda_descripcion import busqueda_descripcion

    # Barra de búsqueda
    lblframe_busqueda_detalle_venta = tb.LabelFrame(master = parent.frame_detalle_venta)
    lblframe_busqueda_detalle_venta.grid(row = 1, column = 0, sticky = NSEW)

    parent.btn_busqueda_codigo = tb.Button(master = lblframe_busqueda_detalle_venta, text = ' # ', 
                                             bootstyle = 'success-outline', 
                                             command = lambda: busqueda_descripcion(parent))
    parent.btn_busqueda_codigo.grid(row = 0, column = 0, padx = 5, pady = 10)

    # Etiqueta para la barra de búsqueda
    parent.ent_buscar_codigo_detalle_venta = tb.Entry(master = lblframe_busqueda_detalle_venta, width = 100, 
                                               bootstyle = 'info')
    parent.ent_buscar_codigo_detalle_venta.grid(row = 0, column = 1, padx = 5, pady = 10)
    #parent.ent_buscar_lista_productos.bind('<Key>')
