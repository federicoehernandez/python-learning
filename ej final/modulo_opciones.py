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
        resultado = askcolor(color="#00ff00", title="Seleccione su color preferido")
        raiz.config(bg=resultado[1])

    # Funcion para salir

    def salir(self, raiz):
        raiz.quit()
