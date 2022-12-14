"""
Controlador:
    Este modulo controla el flujo de informacion segun lo que el usuario ejecute.
"""

from tkinter import Tk
from vista import Vista
from modulo_abm import Abm

__author__ = "Federico Emanuel Hernandez"
__maintainer__ = "Federico Emanuel Hernandez"
__email__ = "federico.e.hernandez@gmail.com"
__copyright__ = "Copyright 2022"
__version__ = "0.1"


class Controlador:
    """
    Esta clase se utiliza en su instanciacion para crear la interfaz con la que el usuario va a interactuar.
    """

    def __init__(self, root):
        self.root_controler = root
        self.objeto_vista = Vista(self.root_controler)


if __name__ == "__main__":
    root = Tk()
    Controlador(root)
    root.mainloop()
