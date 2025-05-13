# Importaciones:
import ttkbootstrap as tb
from interfaz.ventana_principal import Ventana

def main():
    """Función principal para ejecutar la aplicación."""
    app = Ventana()
    # Diseño del proyecto
    tb.Style('darkly')
    app.mainloop()

# Ejecutar la aplicación
if __name__ == "__main__":
    main()