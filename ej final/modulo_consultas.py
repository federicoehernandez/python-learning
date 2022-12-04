from modulo_abm import Facturas

from tkinter.messagebox import *


class Consultas:
    def __init__(self):
        pass

    # Funciones para seleccionar todo
    def select_all(self_sa, arbol):
        for item in arbol.get_children():
            self_sa.add_selection(arbol, item)

    def add_selection(self_asel, arbol, item):
        arbol.selection_add(item)

    # Funcion para listar los registros seleccionados:
    def fver(self_fver, arbol):
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
    def listar_c(self_listc, arbol):
        self_listc.select_all(arbol)
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
    def listar_v(self_listv, arbol):
        self_listv.select_all(arbol)
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
    def traer_lista(self_tlist):
        query = Facturas.select()
        listado3 = []
        for fila in query:
            listado3.append(fila.CUIT)
        listado3 = list(set(listado3))

        return listado3

    # Funcion para mostrar el saldo por CUIT
    def ver_saldo(self_vlist, cuit_selected):
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
        list = self.traer_lista()
        boton["values"] = list
