# Importaciones
from ttkbootstrap.scrolled import ScrolledFrame
from tkinter import NSEW

def ventana_busqueda_detalle_venta(parent):
    """ """
    parent.frame_busqueda_detalle_venta = ScrolledFrame(master = parent, 
                                                        width = 100,
                                                        autohide = True)
    parent.frame_busqueda_detalle_venta.grid(row = 0, column = 2, sticky = NSEW)


