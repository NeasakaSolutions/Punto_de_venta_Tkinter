# Importaciones
from tkinter import END
from tkinter import NORMAL

def llenar_entrys_modificar_producto(parent):
    """Funcion para rellenar los datos al modificar algun usuario"""
    
    # Importaciones perezosas
    
    # Borrar cualquier texto existente
    parent.ent_codigo_modificar_producto.delete(0, END)
    parent.ent_nombre_modificar_producto.delete(0, END)
    parent.ent_laboratorio_modificar_producto.delete(0, END)
    parent.ent_costo_modificar_producto.delete(0, END)
    parent.ent_precio_modificar_producto.delete(0, END)
    parent.ent_stock_modificar_producto.delete(0, END)
    parent.ent_minimo_modificar_producto.delete(0, END)

    # Llenar los campos con los valores del usuario seleccionado
    parent.ent_codigo_modificar_producto.config(state = NORMAL)
    parent.ent_codigo_modificar_producto.insert(0, parent.valor_producto_seleccionado[0])
    parent.ent_codigo_modificar_producto.config(state = 'readonly')
    parent.ent_nombre_modificar_producto.insert(0, parent.valor_producto_seleccionado[1])
    parent.ent_laboratorio_modificar_producto.insert(0, parent.valor_producto_seleccionado[2])
    parent.ent_costo_modificar_producto.insert(0, parent.valor_producto_seleccionado[3])
    parent.ent_precio_modificar_producto.insert(0, parent.valor_producto_seleccionado[4])
    parent.ent_stock_modificar_producto.config(state = NORMAL)
    parent.ent_stock_modificar_producto.insert(0, parent.valor_producto_seleccionado[5])
    parent.ent_stock_modificar_producto.config(state = 'readonly')
    parent.ent_minimo_modificar_producto.insert(0, parent.valor_producto_seleccionado[6])
