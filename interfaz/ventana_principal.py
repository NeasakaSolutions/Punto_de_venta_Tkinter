# Importaciones:
import ttkbootstrap as tb
from tkinter import Tk
from interfaz.ventana_login import ventana_login

class Ventana(tb.Window):
    """Clase que representa la ventana principal de la aplicación."""

    def __init__(self):
        """Método para inicializar la ventana principal."""

        super(). __init__()
        # Configuración de la ventana
        self.title("Punto de Venta")
        self.state('zoomed')

        # Llamando a la ventana login:
        ventana_login(self)