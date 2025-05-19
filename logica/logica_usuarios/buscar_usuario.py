# Importaciones:
from base_datos.conexion import conectar

def buscar_usuario(parent, event = None):
    """Funcion que muestra los usuarios atravez de consultas"""

    # conexion a la bd
    mi_conexion = conectar()
    # Crear el cursor
    mi_cursor = mi_conexion.cursor()
    
    # Limpiar el treeview
    registro = parent.tree_lista_usuarios.get_children()
    for elementos in registro:
        parent.tree_lista_usuarios.delete(elementos)

    # Crear la cosulta
    mi_cursor.execute("SELECT * FROM Usuarios WHERE Nombre LIKE ? ORDER BY Clave DESC",
                      (parent.ent_buscar_lista_usuarios.get() + '%',))
    datos_usuarios = mi_cursor.fetchall()

    # insertar las filas en el treeview
    for fila in datos_usuarios:
        parent.tree_lista_usuarios.insert('', 0, fila[0], values = (fila[0], fila[1], fila[2], fila[3]))

    # Aplicar cambios
    mi_conexion.commit()
    # Cerrar conexion
    mi_conexion.close()

