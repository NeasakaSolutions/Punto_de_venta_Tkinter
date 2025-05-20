# Importaciones:
import ttkbootstrap as tb
from tkinter import Frame
from tkinter import W

def ventana_lista_productos(parent):
    """Crea una ventana para mostrar la lista de productos."""

    # Importaciones perezosas
    from interfaz.interfaz_productos.ventana_nuevo_producto import ventana_nuevo_producto
    from interfaz.interfaz_productos.ventana_modificar_producto import ventana_modificar_producto
    from logica.logica_productos.buscar_producto import buscar_producto

    # Crear un marco para la ventana
    parent.frame_lista_productos = Frame(master = parent)
    parent.frame_lista_productos.grid(row = 0, column = 1, columnspan = 2, sticky = "NSEW")

    # Configurar el diseño de la ventana
    lblframe_botones_lista_productos = tb.LabelFrame(master = parent.frame_lista_productos)
    lblframe_botones_lista_productos.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "NSEW")

    # Botón para agregar un nuevo producto
    btn_nuevo_lista_productos = tb.Button(master = lblframe_botones_lista_productos, text = "Nuevo", 
                                         width = 15, bootstyle = "success", 
                                         command = lambda: ventana_nuevo_producto(parent))
    btn_nuevo_lista_productos.grid(row = 0, column = 0, padx = 10, pady = 10)

    # Botón para modificar un producto existente
    btn_modificar_lista_productos = tb.Button(master = lblframe_botones_lista_productos, text = "Modificar", 
                                         width = 15, bootstyle = "warning", 
                                         command = lambda: ventana_modificar_producto(parent))
    btn_modificar_lista_productos.grid(row = 0, column = 1, padx = 10, pady = 10)

    # Botón para eliminar un producto
    btn_eliminar_lista_productos = tb.Button(master = lblframe_botones_lista_productos, text = "Eliminar", 
                                         width = 15, bootstyle = "danger")
    btn_eliminar_lista_productos.grid(row = 0, column = 2, padx = 10, pady = 10)

    # Barra de búsqueda
    lblframe_busqueda_lista_productos = tb.LabelFrame(master = parent.frame_lista_productos)
    lblframe_busqueda_lista_productos.grid(row = 1, column = 0, padx= 5, pady = 5, sticky = "NSEW",)

    # Etiqueta para la barra de búsqueda
    parent.ent_buscar_lista_productos = tb.Entry(master = lblframe_busqueda_lista_productos, width = 114)
    parent.ent_buscar_lista_productos.grid(row = 0, column = 0, padx = 10, pady = 10)
    parent.ent_buscar_lista_productos.bind('<Key>')

    # Botón para buscar un producto
    lblframe_tree_lista_productos = tb.LabelFrame(master = parent.frame_lista_productos)
    lblframe_tree_lista_productos.grid(row = 2, column = 0, padx= 5, pady = 5, sticky = "NSEW",)

    # Crear columnas:
    columnas = ("codigo", "nombre", "laboratorio", "costo", "precio", "stock", "minimo")

    # Crear el Treeview para mostrar la lista de usuarios
    parent.tree_lista_productos = tb.Treeview(master = lblframe_tree_lista_productos, height = 17, 
                                              columns = columnas ,show = "headings", 
                                              bootstyle = "success")
    
    parent.tree_lista_productos.grid(row = 0, column = 0, padx = 10, pady = 10)

    # Crear las cabeceras
    parent.tree_lista_productos.heading('codigo', text = 'Codigo', anchor = W)
    parent.tree_lista_productos.heading('nombre', text = 'Descripcion', anchor = W)
    parent.tree_lista_productos.heading('laboratorio', text = 'Laboratorio', anchor = W)
    parent.tree_lista_productos.heading('costo', text = 'Costo', anchor = W)
    parent.tree_lista_productos.heading('precio', text = 'Precio', anchor = W)
    parent.tree_lista_productos.heading('stock', text = 'Stock', anchor = W)
    parent.tree_lista_productos.heading('minimo', text = 'Minimo', anchor = W)

    # Configurar las columnas a mostrar:
    parent.tree_lista_productos['displaycolumns'] = ('codigo', 'nombre', 'laboratorio', 'precio')

    # Tamanio de las columnas
    parent.tree_lista_productos.column('codigo', width = 100)
    parent.tree_lista_productos.column('nombre', width = 300)
    parent.tree_lista_productos.column('laboratorio', width = 200)
    parent.tree_lista_productos.column('costo', width = 100)
    parent.tree_lista_productos.column('precio', width = 100)
    parent.tree_lista_productos.column('stock', width = 100)
    parent.tree_lista_productos.column('minimo', width = 100)

    # Crear el scrollbar
    tree_scroll = tb.Scrollbar(master = lblframe_tree_lista_productos, bootstyle = "success-round")
    tree_scroll.grid(row = 0, column = 1, padx = 5, pady = 10)

    # Configurar el scrollbar
    tree_scroll.config(command = parent.tree_lista_productos.yview)

    buscar_producto(parent, None)
    parent.ent_buscar_lista_productos.focus()






