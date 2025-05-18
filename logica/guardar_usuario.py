# Importaciones
from tkinter import messagebox
from base_datos.conexion import conectar
from interfaz.ventana_lista_usuarios import ventana_lista_usuarios

def guardar_usuario(parent):
    """Configuracion para el guardado de usuarios """

    if (parent.ent_codigo_nuevo_usuario.get() == '' or parent.ent_nombre_nuevo_usuario.get() == ''
        or parent.ent_clave_nuevo_usuario.get() == '' or parent.cbo_rol_nuevo_usuario.get() == ''):
            messagebox.showerror('Guardando usuario', 'Favor de llenar todos los campos.')
            return
    
    try:
        # conexion a la bd
        mi_conexion = conectar()
        # Crear el cursor
        mi_cursor = mi_conexion.cursor()

        guardar_datos_usuario = (parent.ent_codigo_nuevo_usuario.get(), parent.ent_nombre_nuevo_usuario.get(), 
                                parent.ent_clave_nuevo_usuario.get(), parent.cbo_rol_nuevo_usuario.get())

        # Crear la cosulta
        mi_cursor.execute("INSERT INTO Usuarios VALUES (?, ?, ?, ?)", (guardar_datos_usuario))

        # Aplicar cambios
        mi_conexion.commit()

        # Avisar que se guardo
        messagebox.showinfo('Guardando usuario', 'Registro guardado correctamente.')
        parent.frame_nuevo_usuario.destroy()
        ventana_lista_usuarios(parent)

        # Cerrar conexion
        mi_conexion.close()
    except:
         messagebox.showerror('Guardando usuario', 'Ocurrio un error.')




