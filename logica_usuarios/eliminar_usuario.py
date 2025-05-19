# Importaciones
from tkinter import messagebox
from base_datos.conexion import conectar

def eliminar_usuario(parent):
    """Funcion que contiene la configuracion para la eliminacion de usuarios"""

    # Importaciones perezosas
    from logica_usuarios.buscar_usuario import buscar_usuario


    usuario_seleccionado_eliminar = parent.tree_lista_usuarios.focus()
    valor_usuario_seleccionado_eliminar = parent.tree_lista_usuarios.item(usuario_seleccionado_eliminar,
                                            'values' )
    
    try:
        if valor_usuario_seleccionado_eliminar != '':
            respuesta = messagebox.askquestion('Eliminando usuario', 
                                            '¿Esta seguro de eliminar el usuario seleccionado?')
            if respuesta == 'yes':
                # conexion a la bd
                mi_conexion = conectar()
                # Crear el cursor
                mi_cursor = mi_conexion.cursor()

                # Crear la consulta
                mi_cursor.execute("DELETE FROM Usuarios WHERE Codigo =" 
                                + str(valor_usuario_seleccionado_eliminar[0]))

                # Aplicar cambios
                mi_conexion.commit()
                messagebox.showinfo('Eliminando usuario', 'Registro eliminado correctamente')
                buscar_usuario(parent)
                # Cerrar conexion
                mi_conexion.close()

            else:
                messagebox.showerror('Eliminando usuario', 'Eliminacion cancelada')
    except:
        messagebox.showerror('Eliminando usuario', 'Ocurrio un error')


