# Importaciones
import ttkbootstrap as tb
from tkinter import NSEW


def busqueda_descripcion(parent):
    """Funcion para la configuracion de la barra de busqueda"""

    # Importaciones perezosas
    from interfaz.interfaz_detalle_de_venta.busqueda_codigo import busqueda_codigo

    # Barra de búsqueda
    lblframe_busqueda_detalle_venta = tb.LabelFrame(master = parent.frame_detalle_venta)
    lblframe_busqueda_detalle_venta.grid(row = 1, column = 0, sticky = NSEW)

    parent.btn_busqueda_descripcion = tb.Button(master = lblframe_busqueda_detalle_venta, text = 'abc', 
                                             bootstyle = 'success-outline', 
                                             command = lambda: busqueda_codigo(parent))
    parent.btn_busqueda_descripcion.grid(row = 0, column = 0, padx = 5, pady = 10)

    # Etiqueta para la barra de búsqueda
    parent.ent_buscar_detalle_venta = tb.Entry(master = lblframe_busqueda_detalle_venta, width = 99,
                                               bootstyle = 'info')
    parent.ent_buscar_detalle_venta.grid(row = 0, column = 1, padx = 5, pady = 10)
    #parent.ent_buscar_detalle_venta.bind('<Key>')
