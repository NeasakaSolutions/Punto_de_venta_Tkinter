# Importaciones



def pasar_codigo_detalle_venta(parent, codigo_seleccionado_detalle_venta):
    """ Pasa el código del producto seleccionado en la búsqueda de detalle de venta
    al campo de entrada correspondiente."""

    parent.ent_buscar_detalle_venta.insert(0, codigo_seleccionado_detalle_venta)