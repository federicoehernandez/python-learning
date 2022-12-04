from tkinter import Tk
from vista import Vista
from modulo_abm import Abm


class Controlador:
    def __init__(self_icont, root):
        self_icont.root_controler = root
        self_icont.objeto_vista = Vista(self_icont.root_controler)


if __name__ == "__main__":
    root = Tk()
    Controlador(root)
    root.mainloop()
