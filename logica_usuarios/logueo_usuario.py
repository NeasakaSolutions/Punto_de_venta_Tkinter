# Importaciones:
from interfaz_usuarios.ventana_menu import ventana_menu
from base_datos.conexion import conectar
from tkinter import messagebox

def logueo_usuarios(parent):
    """Funcion para validar el acceso al punto de venta"""

    try:
        # Conexion a la bd
        mi_conexion = conectar()
        # Crear cursor
        mi_cursor = mi_conexion.cursor()

        # Obtenemos la informacion que el usuario proporciona
        con_usuario = parent.ent_usuario.get()
        con_clave = parent.ent_clave.get()

        # Crecion de la consulta
        mi_cursor.execute("SELECT * FROM Usuarios WHERE Nombre = ? AND Clave = ?",
                        (con_usuario, con_clave))
        datos_logueo = mi_cursor.fetchall()

        # Validar que los datos sean correctos
        if datos_logueo != '':
            for fila in datos_logueo:
                nombre_usuario_logueado = fila[1]
                clave_usuario_logueado = fila[2]
            if (nombre_usuario_logueado == parent.ent_usuario.get() and
                clave_usuario_logueado == parent.ent_clave.get()):
                parent.frame_login.destroy()
                # Llamado a la funcion
                ventana_menu(parent)

        # Aplicar cambios
        mi_conexion.commit()
        # Cerrar conexion
        mi_conexion.close()
    except:
        messagebox.showwarning('Logueo', 'El usuario o la clave son incorrectas, por favor revisa.')

    


