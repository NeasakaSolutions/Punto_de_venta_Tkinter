# Importaciones:
from tkinter import Frame
from tkinter import Button
from tkinter import LabelFrame

def ventana_lista_usuarios(parent):
    """Crea una ventana para mostrar la lista de usuarios."""

    # Crear un marco para la ventana
    parent.frame_lista_usuarios = Frame(master = parent)
    parent.frame_lista_usuarios.grid(row = 0, column = 1, columnspan = 2, sticky = "NSEW")

    lblframe_botones_lista_usuarios = LabelFrame(master = parent.frame_lista_usuarios)
    lblframe_botones_lista_usuarios.grid(row = 0, column = 0, sticky = "NSEW")

    btn_nuevo_lista_usuarios = Button(master = lblframe_botones_lista_usuarios, text = "Nuevo Usuario",
                                      width = 15)
    btn_nuevo_lista_usuarios.grid(row = 0, column = 0, padx = 10, pady = 10)



