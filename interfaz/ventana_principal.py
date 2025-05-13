# Importaciones:
from tkinter import Tk

class Ventana(Tk):
    """Clase que representa la ventana principal de la aplicación."""

    def __init__(self):
        """Método para inicializar la ventana principal."""

        super(). __init__()
        # Configuración de la ventana
        self.title("Punto de Venta")
        self.state('zoomed')