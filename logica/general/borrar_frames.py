# Importaciones


def borrar_frames(parent):
    for frames in parent.frame_center.winfo_children():
        frames.destroy()


