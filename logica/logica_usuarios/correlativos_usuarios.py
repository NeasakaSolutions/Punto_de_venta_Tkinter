# Importaciones:
from tkinter import NORMAL
from tkinter import messagebox
from base_datos.conexion import conectar

def correlativo_usuarios(parent):
    """Funcion que ordena las id de los usuarios"""

    try:
        # conexion a la bd
        mi_conexion = conectar()
        # Crear el cursor
        mi_cursor = mi_conexion.cursor()

        # Crear la cosulta
        mi_cursor.execute("SELECT MAX(Codigo) FROM Usuarios")
        correlativo_usuarios = mi_cursor.fetchone()

        for datos in correlativo_usuarios:
            if datos == None:
                parent.nuevo_correlativo_usuario = (int(1))
                parent.ent_codigo_nuevo_usuario.config(state = NORMAL)
                parent.ent_codigo_nuevo_usuario.insert(0, parent.nuevo_correlativo_usuario)
                parent.ent_codigo_nuevo_usuario.config(state = 'readonly')
            else:
                parent.nuevo_correlativo_usuario = (int(datos) + 1)
                parent.ent_codigo_nuevo_usuario.config(state = NORMAL)
                parent.ent_codigo_nuevo_usuario.insert(0, parent.nuevo_correlativo_usuario)
                parent.ent_codigo_nuevo_usuario.config(state = 'readonly')

        # Aplicar cambios
        mi_conexion.commit()
        # Cerrar conexion
        mi_conexion.close()

    except:
        messagebox.showerror('Correlativo usuarios', 'Ocurrio un error')

