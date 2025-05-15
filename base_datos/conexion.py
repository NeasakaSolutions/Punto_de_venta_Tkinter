import sqlite3

def conectar():
    """Funcion que hace conexión a la base de datos con manejo de errores"""
    try:
        conexion = sqlite3.connect("base_datos/punto_venta.db")
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

