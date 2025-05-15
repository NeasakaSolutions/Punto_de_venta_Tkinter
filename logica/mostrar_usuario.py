# Importaciones:
from base_datos.conexion import conectar

def mostrar_usuario():
    """Funcio que muestra los usuarios atravez de consultas"""

    # conexion a la bd
    mi_conexion = conectar()
    # Crear el cursor
    mi_cursor = mi_conexion.cursor()
    # Crear la cosulta
    mi_cursor.execute("SELECT * FROM Usuarios")
    datos_usuarios = mi_cursor.fetchall()
    print(datos_usuarios)

    # Aplicar cambios
    mi_conexion.commit()
    # Cerrar conexion
    mi_conexion.close()

