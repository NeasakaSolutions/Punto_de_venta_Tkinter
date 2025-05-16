# Importaciones:
import ttkbootstrap as tb
from tkinter import Toplevel
from tkinter import Label

def ventana_nuevo_usuario(parent):
    """Interfaz para la creacion del un nuevo usuario"""

    # Configuracion de la ventana
    parent.frame_nuevo_usuario = Toplevel(master = parent)
    parent.frame_nuevo_usuario.title('Nuevo Usuario')
    parent.frame_nuevo_usuario.geometry('400x350')
    parent.frame_nuevo_usuario.grab_set()

    lblframe_nuevo_usuario = tb.LabelFrame(master = parent.frame_nuevo_usuario, text = 'Nuevo Usuario')
    lblframe_nuevo_usuario.pack(padx = 15, pady = 35)

    # Codigo
    lbl_codigo_nuevo_usuario = Label(master = lblframe_nuevo_usuario, text = 'Codigo')
    lbl_codigo_nuevo_usuario.grid(row = 0, column = 0, padx = 10, pady = 10)
    ent_codigo_nuevo_usuario = tb.Entry(master = lblframe_nuevo_usuario, width = 40)
    ent_codigo_nuevo_usuario.grid(row = 0, column = 1, padx = 10, pady = 10)

    # Nombre
    lbl_nombre_nuevo_usuario = Label(master = lblframe_nuevo_usuario, text = 'Nombre')
    lbl_nombre_nuevo_usuario.grid(row = 1, column = 0, padx = 10, pady = 10)
    ent_nombre_nuevo_usuario = tb.Entry(master = lblframe_nuevo_usuario, width = 40)
    ent_nombre_nuevo_usuario.grid(row = 1, column = 1, padx = 10, pady = 10)

    # Clave
    lbl_clave_nuevo_usuario = Label(master = lblframe_nuevo_usuario, text = 'Clave')
    lbl_clave_nuevo_usuario.grid(row = 2, column = 0, padx = 10, pady = 10)
    ent_clave_nuevo_usuario = tb.Entry(master = lblframe_nuevo_usuario, width = 40)
    ent_clave_nuevo_usuario.grid(row = 2, column = 1, padx = 10, pady = 10)
    ent_clave_nuevo_usuario.config(show = '*')

    # Rol
    lbl_rol_nuevo_usuario = Label(master = lblframe_nuevo_usuario, text = 'Rol')
    lbl_rol_nuevo_usuario.grid(row = 3, column = 0, padx = 10, pady = 10)
    cbo_rol_nuevo_usuario = tb.Combobox(master = lblframe_nuevo_usuario, width = 38, 
                                         values = ['Administrador', 'Bodega', 'Vendedor'])
    cbo_rol_nuevo_usuario.grid(row = 3, column = 1, padx = 10, pady = 10)
    cbo_rol_nuevo_usuario.current(0)
    cbo_rol_nuevo_usuario.config(state = 'readonly')

    # COnfiguracion del boton para guardar usuario
    btn_guardar_usuario = tb.Button(master = lblframe_nuevo_usuario, text = 'Guardar', width = 38,
                                    bootstyle = 'success')
    btn_guardar_usuario.grid(row = 4, column = 1, padx = 10, pady = 10)






