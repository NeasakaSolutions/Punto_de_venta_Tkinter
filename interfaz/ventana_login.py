# Importaciones:
from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import LabelFrame
from tkinter import Entry
from tkinter import ttk

def ventana_login(parent):
    """Función para crear la ventana de inicio de sesión."""

    # Posicionamiento de la ventana
    parent.grid_columnconfigure(0, weight = 1)

    # Configuración del contenedor principal de la ventana login
    parent.frame_login = Frame(master = parent)
    parent.frame_login.grid(row = 0, column = 0, sticky = "NSEW")

    # Creación de un marco para el inicio de sesión
    lblframe_login = LabelFrame(master = parent.frame_login, text = "Acceso")
    lblframe_login.pack(padx = 10, pady = 35)

    # Creación de etiquetas y campos de entrada
    lbl_titulo = Label(master = lblframe_login, text = "Iniciar sesion")
    lbl_titulo.pack(padx = 10, pady = 35)

    # Etiquetas para usuario y clave
    ent_usuario = ttk.Entry(master = lblframe_login, width = 40, justify = "center")
    ent_usuario.pack(padx = 10, pady = 5)
    ent_clave = ttk.Entry(master = lblframe_login, width = 40, justify = "center")
    ent_clave.pack(padx = 10, pady = 5)
    # Ocultando la clave
    ent_clave.config(show = "*")
    btn_acceso = ttk.Button(master = lblframe_login, width = 38, text = "Login")
    btn_acceso.pack(padx = 10, pady = 5)




