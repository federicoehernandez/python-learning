"""
Modulo Opciones:
    En este modulo se encuentran todas las acciones que tendrá el usuario que no tengan que ver con acciones sobre la base de datos directamente, como cerrar el programa y cambiar colores de la ventana.
"""

from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.messagebox import *


class Opciones:
    def __init__(
        self,
    ):
        pass

    # Funcion para elegir un color de tema:
    def elegir_color(self, raiz):
        """
        El metodo **elegir_color** cambia el color del fondo de la ventana por el que el usuario seleccione.
        """
        resultado = askcolor(color="#00ff00", title="Seleccione su color preferido")
        raiz.config(bg=resultado[1])

    # Funcion para salir

    def salir(self, raiz):
        """
        El metodo **salir** siplemente finaliza el programa.
        """
        raiz.quit()
