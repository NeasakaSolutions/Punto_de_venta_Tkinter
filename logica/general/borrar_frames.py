# Importaciones


def borrar_frames(parent):
    for frames in parent.frame_center.winfo_children():
        frames.destroy()

    parent.frame_busqueda_detalle_venta.grid_forget()



