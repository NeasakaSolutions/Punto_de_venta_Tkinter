# Importaciones
from tkinter import messagebox
from base_datos.conexion import conectar


def modificar_usuario(parent):
    """Configuracion para la modificacion de usuarios """

    # Importaciones perezosas

    if (parent.ent_codigo_modificar_usuario.get() == '' or parent.ent_nombre_modificar_usuario.get() == ''
        or parent.ent_clave_modificar_usuario.get() == '' or parent.cbo_rol_modificar_usuario.get() == ''):
            messagebox.showerror('Modificando usuario', 'Favor de llenar todos los campos.')
            return
    
    try:
        # conexion a la bd
        mi_conexion = conectar()
        # Crear el cursor
        mi_cursor = mi_conexion.cursor()

        modificar_datos_usuario = (parent.ent_nombre_modificar_usuario.get(), 
                                 parent.ent_clave_modificar_usuario.get(), parent.cbo_rol_modificar_usuario.get())

        # Crear la cosulta
        mi_cursor.execute("UPDATE Usuarios SET Nombre = ?, Clave = ?, Rol = ? WHERE Codigo = " 
                          + parent.ent_codigo_modificar_usuario.get(), 
                          (modificar_datos_usuario))

        # Aplicar cambios
        mi_conexion.commit()

        # Avisar que se guardo
        messagebox.showinfo('Modificando usuario', 'Registro modificado correctamente.')

        parent.valor_usuario_seleccionado = parent.tree_lista_usuarios.item(parent.usuario_seleccionado,
                                            text = '', values = (parent.ent_codigo_modificar_usuario.get(), 
                                            parent.ent_nombre_modificar_usuario.get(), 
                                            parent.ent_clave_modificar_usuario.get(), 
                                            parent.cbo_rol_modificar_usuario.get()))
        
        parent.frame_modificar_usuario.destroy()

        # Cerrar conexion
        mi_conexion.close()
    except:
         messagebox.showerror('Modificando usuario', 'Ocurrio un error.')

