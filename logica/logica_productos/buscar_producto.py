# Importaciones:
from tkinter import messagebox
from base_datos.conexion import conectar

def buscar_producto(parent, event = None):
    """Funcion que muestra los productos atravez de consultas"""

    try:
        # conexion a la bd
        mi_conexion = conectar()
        # Crear el cursor
        mi_cursor = mi_conexion.cursor()
        
        # Limpiar el treeview
        registro = parent.tree_lista_productos.get_children()
        for elementos in registro:
            parent.tree_lista_productos.delete(elementos)

        # Crear la cosulta
        mi_cursor.execute("SELECT * FROM Productos WHERE Nombre LIKE ?",
                        (parent.ent_buscar_lista_productos.get() + '%',))
        datos_productos = mi_cursor.fetchall()

        # insertar las filas en el treeview
        for fila in datos_productos:
            parent.tree_lista_productos.insert('', 0, fila[0], values = (fila[0], fila[1], fila[2], fila[3],
                                                fila[4], fila[5], fila[6]))

        # Aplicar cambios
        mi_conexion.commit()
        # Cerrar conexion
        mi_conexion.close()
    
    except:
        messagebox.showerror('Buscar producto', 'Ocurrio un error')

