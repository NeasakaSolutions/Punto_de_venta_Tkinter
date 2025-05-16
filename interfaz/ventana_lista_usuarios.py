# Importaciones:
import ttkbootstrap as tb
from tkinter import Frame
from tkinter import Entry
from tkinter import LabelFrame
from tkinter import ttk
from tkinter import W
from logica.mostrar_usuario import mostrar_usuarios

def ventana_lista_usuarios(parent):
    """Crea una ventana para mostrar la lista de usuarios."""

    # Crear un marco para la ventana
    parent.frame_lista_usuarios = Frame(master = parent)
    parent.frame_lista_usuarios.grid(row = 0, column = 1, columnspan = 2, sticky = "NSEW")

    # Configurar el diseño de la ventana
    lblframe_botones_lista_usuarios = tb.LabelFrame(master = parent.frame_lista_usuarios)
    lblframe_botones_lista_usuarios.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "NSEW")

    # Botón para agregar un nuevo usuario
    btn_nuevo_lista_usuarios = tb.Button(master = lblframe_botones_lista_usuarios, text = "Nuevo", 
                                         width = 15, bootstyle = "success")
    btn_nuevo_lista_usuarios.grid(row = 0, column = 0, padx = 10, pady = 10)

    # Botón para modificar un usuario existente
    btn_modificar_lista_usuarios = tb.Button(master = lblframe_botones_lista_usuarios, text = "Modificar", 
                                         width = 15, bootstyle = "warning")
    btn_modificar_lista_usuarios.grid(row = 0, column = 1, padx = 10, pady = 10)

    # Botón para eliminar un usuario
    btn_eliminar_lista_usuarios = tb.Button(master = lblframe_botones_lista_usuarios, text = "Eliminar", 
                                         width = 15, bootstyle = "danger")
    btn_eliminar_lista_usuarios.grid(row = 0, column = 2, padx = 10, pady = 10)

    # Barra de búsqueda
    lblframe_busqueda_lista_usuarios = tb.LabelFrame(master = parent.frame_lista_usuarios)
    lblframe_busqueda_lista_usuarios.grid(row = 1, column = 0, padx= 5, pady = 5, sticky = "NSEW",)

    # Etiqueta para la barra de búsqueda
    ent_buscar_lista_usuarios = tb.Entry(master = lblframe_busqueda_lista_usuarios, width = 98)
    ent_buscar_lista_usuarios.grid(row = 0, column = 0, padx = 10, pady = 10)

    # Botón para buscar un usuario
    lblframe_tree_lista_usuarios = tb.LabelFrame(master = parent.frame_lista_usuarios)
    lblframe_tree_lista_usuarios.grid(row = 2, column = 0, padx= 5, pady = 5, sticky = "NSEW",)

    # Crear columnas:
    columnas = ("codigo", "nombre", "clave", "rol")

    # Crear el Treeview para mostrar la lista de usuarios
    parent.tree_lista_usuarios = ttk.Treeview(master = lblframe_tree_lista_usuarios, height = 17, 
                                              columns = columnas ,show = "headings", 
                                              bootstyle = "success")
    
    parent.tree_lista_usuarios.grid(row = 0, column = 0, padx = 10, pady = 10)

    # Crear las cabeceras
    parent.tree_lista_usuarios.heading('codigo', text = 'Codigo', anchor = W)
    parent.tree_lista_usuarios.heading('nombre', text = 'Nombre', anchor = W)
    parent.tree_lista_usuarios.heading('clave', text = 'Clave', anchor = W)
    parent.tree_lista_usuarios.heading('rol', text = 'Rol', anchor = W)

    # Tamanio de las columnas
    parent.tree_lista_usuarios.column('codigo', width = 100)
    parent.tree_lista_usuarios.column('nombre', width = 300)
    parent.tree_lista_usuarios.column('clave', width = 100)
    parent.tree_lista_usuarios.column('rol', width = 200)

    # Configurar las columnas a mostrar:
    parent.tree_lista_usuarios['displaycolumns'] = ('codigo', 'nombre', 'rol')


    # Crear el scrollbar
    tree_scroll = tb.Scrollbar(master = lblframe_tree_lista_usuarios, bootstyle = "success-round")
    tree_scroll.grid(row = 0, column = 1, padx = 5, pady = 10)

    # Configurar el scrollbar
    tree_scroll.config(command = parent.tree_lista_usuarios.yview)

    mostrar_usuarios(parent)






