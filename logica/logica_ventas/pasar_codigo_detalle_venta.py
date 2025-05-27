# Importaciones

def pasar_codigo_detalle_venta(parent, codigo_seleccionado_detalle_venta):
    """ Pasa el código del producto seleccionado en la búsqueda de detalle de venta
    al campo de entrada correspondiente."""

    # Importaciones perezosas
    from logica.logica_ventas.producto_seleccionado_detalle_venta import producto_seleccionado_detalle_venta

    parent.ent_buscar_codigo_detalle_venta.insert(0, codigo_seleccionado_detalle_venta)
    producto_seleccionado_detalle_venta(parent)