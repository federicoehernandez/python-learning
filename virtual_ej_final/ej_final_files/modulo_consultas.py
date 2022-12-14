"""
Modulo consultas:
    En este modulo se encuentran todas las operaciones que representen extraccion y visualizacion de informacion que esté en la base de datos y el treeview.
"""

from modulo_abm import Facturas
from tkinter.messagebox import *


class Consultas:
    """
    En la clase **Consultas** se encuentran todos los metodos que ejecutara el usuario desde la interfaz para acceder a informacion que se encuentre en la base de datos.
    """

    def __init__(self):
        pass

    # Funciones para seleccionar todo
    def select_all(self, arbol):
        """
        El metodo **select_all** servira para que el usuario pueda seleccionar todas las lineas del treeview y pueda realizar una accion con ellas.
        """
        for item in arbol.get_children():
            self.add_selection(arbol, item)

    def add_selection(self, arbol, item):
        """
        El metodo **add_selection** complementa al metodo **select_all** para cubrir la funcionalidad de seleccionar todos los registros en el treeview.
        """
        arbol.selection_add(item)

    # Funcion para listar los registros seleccionados:
    def fver(self, arbol):
        """
        El metodo **fver** sirve para visualizar las lineas seleccionadas del treeview en la consola.
        """
        for register in arbol.selection():
            print(
                "ID: "
                + str(arbol.item(register)["text"])
                + " / CUIT: "
                + str((arbol.item(register)["values"])[0])
                + " / RAZON SOCIAL: "
                + str((arbol.item(register)["values"])[1])
                + " / NUMERO DE FACTURA: "
                + str((arbol.item(register)["values"])[2])
                + " / FECHA: "
                + str((arbol.item(register)["values"])[3])
                + " / PRECIO: "
                + str((arbol.item(register)["values"])[4])
                + " / CANTIDAD: "
                + str((arbol.item(register)["values"])[5])
                + " / ALICUOTA: "
                + str((arbol.item(register)["values"])[6])
                + " / IMPUESTO: "
                + str((arbol.item(register)["values"])[7])
                + " / NETO: "
                + str((arbol.item(register)["values"])[8])
                + " / TOTAL: "
                + str((arbol.item(register)["values"])[9])
                + " / COMPRA/VENTA: "
                + (arbol.item(register)["values"])[10]
            )

    # Funcion para listar compras en consola
    def listar_c(self, arbol):
        """
        El metodo **listar_c** sirve para que el usuario pueda ver todas las lineas que representen compras hechas a traves de la consola.
        """
        self.select_all(arbol)
        for register in arbol.selection():
            if (arbol.item(register)["values"])[10] == "Compra":
                print(
                    "ID: "
                    + str(arbol.item(register)["text"])
                    + " / CUIT: "
                    + str((arbol.item(register)["values"])[0])
                    + " / RAZON SOCIAL: "
                    + str((arbol.item(register)["values"])[1])
                    + " / NUMERO DE FACTURA: "
                    + str((arbol.item(register)["values"])[2])
                    + " / FECHA: "
                    + str((arbol.item(register)["values"])[3])
                    + " / PRECIO: "
                    + str((arbol.item(register)["values"])[4])
                    + " / CANTIDAD: "
                    + str((arbol.item(register)["values"])[5])
                    + " / ALICUOTA: "
                    + str((arbol.item(register)["values"])[6])
                    + " / IMPUESTO: "
                    + str((arbol.item(register)["values"])[7])
                    + " / NETO: "
                    + str((arbol.item(register)["values"])[8])
                    + " / TOTAL: "
                    + str((arbol.item(register)["values"])[9])
                    + " / COMPRA/VENTA: "
                    + (arbol.item(register)["values"])[10]
                )

    # Funcion para listar ventas en consola
    def listar_v(self, arbol):
        """
        El metodo **listar_v** sirve para que el usuario pueda ver todas las lineas que representen ventas hechas a traves de la consola.
        """
        self.select_all(arbol)
        for register in arbol.selection():
            if (arbol.item(register)["values"])[10] == "Venta":
                print(
                    "ID: "
                    + str(arbol.item(register)["text"])
                    + " / CUIT: "
                    + str((arbol.item(register)["values"])[0])
                    + " / RAZON SOCIAL: "
                    + str((arbol.item(register)["values"])[1])
                    + " / NUMERO DE FACTURA: "
                    + str((arbol.item(register)["values"])[2])
                    + " / FECHA: "
                    + str((arbol.item(register)["values"])[3])
                    + " / PRECIO: "
                    + str((arbol.item(register)["values"])[4])
                    + " / CANTIDAD: "
                    + str((arbol.item(register)["values"])[5])
                    + " / ALICUOTA: "
                    + str((arbol.item(register)["values"])[6])
                    + " / IMPUESTO: "
                    + str((arbol.item(register)["values"])[7])
                    + " / NETO: "
                    + str((arbol.item(register)["values"])[8])
                    + " / TOTAL: "
                    + str((arbol.item(register)["values"])[9])
                    + " / COMPRA/VENTA: "
                    + (arbol.item(register)["values"])[10]
                )

    # Funcion para traer la lista de cuits unicos al combobox "Seleccinoar CUIT"
    def traer_lista(self):
        """
        El metodo **traer_lista** devuelve un listado de **CUITS** unicos que se utilizan en para mostrar en el combobox de la vista.
        """
        query = Facturas.select()
        listado3 = []
        for fila in query:
            listado3.append(fila.CUIT)
        listado3 = list(set(listado3))

        return listado3

    # Funcion para mostrar el saldo por CUIT
    def ver_saldo(self, cuit_selected):
        """
        El metodo **ver_saldo** sirve para mostrar por interfaz el total adeduado o a favor que se tiene con una **CUIT** en particular.
        """
        print(cuit_selected.get())
        query = Facturas.select(Facturas.Total, Facturas.Compra_Venta).where(
            Facturas.CUIT == cuit_selected.get()
        )

        lista3 = 0
        for x in query:

            if (x.Total, x.Compra_Venta)[1] == "Compra":
                print((x.Total, x.Compra_Venta)[1])
                print((x.Total, x.Compra_Venta)[0])
                lista3 -= (x.Total, x.Compra_Venta)[0]

            else:
                lista3 += (x.Total, x.Compra_Venta)[0]
        print(round(lista3, 2))
        showinfo(
            "Consulta de saldo",
            "Saldo con el cuit " + cuit_selected.get() + ": $" + str(round(lista3, 2)),
        )

    def updtcblist(self, boton):
        """
        El metodo **updtcblist** sirve para que el combobox mantenga el listado de **CUITS** actualizado mientras se esté ejecutando el programa y se realicen modificaciones sobre la base de datos.
        """
        list = self.traer_lista()
        boton["values"] = list
