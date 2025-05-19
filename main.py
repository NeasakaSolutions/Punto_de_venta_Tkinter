# Importaciones:
import ttkbootstrap as tb
from interfaz.interfaz_usuarios.ventana_principal import Ventana

def main():
    """Función principal para ejecutar la aplicación."""
    app = Ventana()
    
    ###Posibles disenios:
    # cosmo (Blanco)
    # darkly (Obscuro)
    # superhero (Claro)
    # solar (Claro)###
    tb.Style('superhero')
    app.mainloop()

# Ejecutar la aplicación
if __name__ == "__main__":
    main()