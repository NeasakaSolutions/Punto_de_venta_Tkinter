# Importaciones:
import ttkbootstrap as tb
from tkinter import Toplevel
from tkinter import Label

def ventana_modificar_usuario(parent):
    """Interfaz para la modificacion de un usuario"""

    # Importaciones perezosas
    from logica.llenar_entrys import llenar_entrys_modificar_usuario

    parent.usuario_seleccionado = parent.tree_lista_usuarios.focus()
    parent.valor_usuario_seleccionado = parent.tree_lista_usuarios.item(parent.usuario_seleccionado, 'values')

    if parent.valor_usuario_seleccionado != '':
        # Configuracion de la ventana
        parent.frame_modificar_usuario = Toplevel(master = parent)
        parent.frame_modificar_usuario.title('Nuevo Usuario')
        parent.frame_modificar_usuario.geometry('400x350')
        parent.frame_modificar_usuario.grab_set()

        lblframe_modificar_usuario = tb.LabelFrame(master = parent.frame_modificar_usuario,
                                                    text = 'Modificar usuario')
        lblframe_modificar_usuario.pack(padx = 15, pady = 35)

        # Codigo
        lbl_codigo_modificar_usuario = Label(master = lblframe_modificar_usuario, text = 'Codigo')
        lbl_codigo_modificar_usuario.grid(row = 0, column = 0, padx = 10, pady = 10)
        parent.ent_codigo_modificar_usuario = tb.Entry(master = lblframe_modificar_usuario, width = 40)
        parent.ent_codigo_modificar_usuario.grid(row = 0, column = 1, padx = 10, pady = 10)

        # Nombre
        lbl_nombre_modificar_usuario = Label(master = lblframe_modificar_usuario, text = 'Nombre')
        lbl_nombre_modificar_usuario.grid(row = 1, column = 0, padx = 10, pady = 10)
        parent.ent_nombre_modificar_usuario = tb.Entry(master = lblframe_modificar_usuario, width = 40)
        parent.ent_nombre_modificar_usuario.grid(row = 1, column = 1, padx = 10, pady = 10)

        # Clave
        lbl_clave_modificar_usuario = Label(master = lblframe_modificar_usuario, text = 'Clave')
        lbl_clave_modificar_usuario.grid(row = 2, column = 0, padx = 10, pady = 10)
        parent.ent_clave_modificar_usuario = tb.Entry(master = lblframe_modificar_usuario, width = 40)
        parent.ent_clave_modificar_usuario.grid(row = 2, column = 1, padx = 10, pady = 10)
        parent.ent_clave_modificar_usuario.config(show = '*')

        # Rol
        lbl_rol_modificar_usuario = Label(master = lblframe_modificar_usuario, text = 'Rol')
        lbl_rol_modificar_usuario.grid(row = 3, column = 0, padx = 10, pady = 10)
        parent.cbo_rol_modificar_usuario = tb.Combobox(master = lblframe_modificar_usuario, width = 38, 
                                            values = ['Administrador', 'Bodega', 'Vendedor'])
        parent.cbo_rol_modificar_usuario.grid(row = 3, column = 1, padx = 10, pady = 10)

        # COnfiguracion del boton para modificar usuario
        btn_modificar_usuario = tb.Button(master = lblframe_modificar_usuario, text = 'Modificar', width = 38,
                                        bootstyle = 'warning')
        btn_modificar_usuario.grid(row = 4, column = 1, padx = 10, pady = 10)

        llenar_entrys_modificar_usuario(parent)



