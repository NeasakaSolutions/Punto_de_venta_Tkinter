# Importaciones:
import ttkbootstrap as tb
from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import LabelFrame
from tkinter import Entry
from tkinter import ttk

def ventana_login(parent):
    """Función para crear la ventana de inicio de sesión."""

    # Importaciones perezosas
    from logica.logueo_usuario import logueo_usuarios

    # Posicionamiento de la ventana
    parent.grid_columnconfigure(1, weight = 1)

    # Configuración del contenedor principal de la ventana login
    parent.frame_login = Frame(master = parent)
    parent.frame_login.grid(row = 0, column = 1, sticky = "NSEW")

    # Creación de un marco para el inicio de sesión
    lblframe_login = tb.LabelFrame(master = parent.frame_login, text = "Acceso")
    lblframe_login.pack(padx = 10, pady = 35)

    # Creación de etiquetas y campos de entrada
    lbl_titulo = tb.Label(master = lblframe_login, text = "Iniciar sesion", font = ("Calibri", 18))
    lbl_titulo.pack(padx = 10, pady = 35)

    # Etiquetas para usuario y clave
    parent.ent_usuario = tb.Entry(master = lblframe_login, width = 40, justify = "center")
    parent.ent_usuario.pack(padx = 10, pady = 5)
    parent.ent_clave = tb.Entry(master = lblframe_login, width = 40, justify = "center")
    parent.ent_clave.pack(padx = 10, pady = 5)
    # Ocultando la clave
    parent.ent_clave.config(show = "*")
    btn_acceso = tb.Button(master = lblframe_login, width = 38, text = "Login", bootstyle = "success",
                           command = lambda: logueo_usuarios(parent))
    btn_acceso.pack(padx = 10, pady = 5)




