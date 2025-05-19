# Importaciones


def centrar_ventana_modificar_usuario(parent, ancho, altura):
    """Configuracion de la ventana"""

    # Atributos
    ventana_ancho = ancho
    ventana_altura = altura

    # Configuracion automatica de la ventana con base al monitor del usuario
    pantalla_ancho = parent.winfo_screenwidth()
    pantalla_alto = parent.winfo_screenheight()

    # Posicion de la ventana
    coordenadas_x = int((pantalla_ancho / 2) - (ventana_ancho / 2 ))
    coordenadas_y = int((pantalla_alto / 2) - (ventana_altura / 2))

    parent.geometry('{}x{}+{}+{}' .format(ventana_ancho, ventana_altura, coordenadas_x, coordenadas_y))
    


