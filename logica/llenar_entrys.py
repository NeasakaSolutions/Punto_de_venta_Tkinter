# Importaciones
from tkinter import END

def llenar_entrys_modificar_usuario(parent):
    """Funcion para rellenar los datos al modificar algun usuario"""
    
    # Importaciones perezosas
    
    # Borrar cualquier texto existente
    parent.ent_codigo_modificar_usuario.delete(0, END)
    parent.ent_nombre_modificar_usuario.delete(0, END)
    parent.ent_clave_modificar_usuario.delete(0, END)
    parent.cbo_rol_modificar_usuario.delete(0, END)

    # Llenar los campos con los valores del usuario seleccionado
    parent.ent_codigo_modificar_usuario.insert(0, parent.valor_usuario_seleccionado[0])
    parent.ent_codigo_modificar_usuario.config(state = 'readonly')
    parent.ent_nombre_modificar_usuario.insert(0, parent.valor_usuario_seleccionado[1])
    parent.ent_clave_modificar_usuario.insert(0, parent.valor_usuario_seleccionado[2])
    parent.cbo_rol_modificar_usuario.insert(0, parent.valor_usuario_seleccionado[3])
    parent.cbo_rol_modificar_usuario.config(state = 'readonly')
