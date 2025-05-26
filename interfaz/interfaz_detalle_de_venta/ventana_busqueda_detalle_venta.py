# Importaciones
from ttkbootstrap.scrolled import ScrolledFrame
from tkinter import NSEW

def ventana_busqueda_detalle_venta(parent):
    """ """
    
    parent.frame_busqueda_detalle_venta = ScrolledFrame(master=parent, width=300, autohide=True)
    parent.frame_busqueda_detalle_venta.grid(row=0, column=2, padx=1, sticky="nsew")
    
    # ¡Importante! Configurar que la columna 2 del parent expanda el frame
    parent.grid_columnconfigure(2, weight=1)
    parent.grid_rowconfigure(0, weight=1)


    #parent.frame_busqueda_detalle_venta = ScrolledFrame(master = parent, 
                                                        #width = 100,
                                                        #autohide = True)
    #parent.frame_busqueda_detalle_venta.grid(row = 0, column = 2, sticky = NSEW)


