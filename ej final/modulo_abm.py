from peewee import *
from playhouse import hybrid
from tkinter.messagebox import *
import datetime
from tkinter import *
from valida_regex import ValidadorRegex
from my_exception import ExceptionOwn

db = SqliteDatabase("facturasdecomprayventa.db")


class BaseModel(Model):
    class Meta:
        database = db


class Facturas(BaseModel):
    id = IntegerField(primary_key=True)
    CUIT = FloatField()
    RazonSocial = CharField()
    Numero_de_factura = IntegerField()
    Fecha = DateField()
    Precio = FloatField()
    Cantidad = IntegerField()
    Alicuota = FloatField()
    Impuesto = FloatField()
    Neto = FloatField()
    Total = FloatField()
    Compra_Venta = CharField()

    @hybrid.hybrid_method
    def gs_impuesto(self):
        return self.Precio * self.Cantidad * self.Alicuota / 100

    @hybrid.hybrid_method
    def gs_neto(self):
        return self.Precio * self.Cantidad

    @hybrid.hybrid_method
    def gs_total(self):
        return (
            self.Precio * self.Cantidad * self.Alicuota / 100
            + self.Precio * self.Cantidad
        )


db.connect()
db.create_tables([Facturas])
db.close()

tuplas = ("30-70836728-8", "Sociedad", 1234)

# db.connect()

factura_consulta = Facturas()

"""

factura_generica = Facturas.create(
    CUIT=tuplas[0],
    RazonSocial=tuplas[1],
    Numero_de_factura=tuplas[2],
    Fecha="2022-11-26",
    Precio=124.60,
    Cantidad=2,
    Alicuota=1.5,
    Impuesto=Facturas.gs_impuesto(),
    Neto=Facturas.gs_neto(),
    Total=Facturas.gs_total(),
    Compra_Venta="Compra",
)
factura_generica.save()
db.close()


db.connect()
factura = Facturas()
factura.CUIT = "30-70836728-9"
factura.RazonSocial = "ASDF2"
factura.Numero_de_factura = 456123
factura.Fecha = "2022-11-27"
factura.Precio = 231.5
factura.Cantidad = 1
factura.Alicuota = 1
factura.Impuesto = Facturas.gs_impuesto()
factura.Neto = Facturas.gs_neto()
factura.Total = Facturas.gs_total()
factura.Compra_Venta = "Compra"
factura.save()
db.close()

"""


class Abm:
    # La funcion de alta de registros:
    def alta2(
        self_a,
        cuitf,
        razonsocialf,
        numerodefacturaf,
        fechaf,
        preciof,
        cantidadf,
        alicuotaf,
        compraventaf,
        arbol,
    ):
        validador = ValidadorRegex(cuitf.get())

        if validador.validator():
            cuit_str = str(cuitf.get())
            cuit_num = [int(x) for x in cuit_str if x != "-"]
            verif = 11 - (
                (
                    cuit_num[0] * 5
                    + cuit_num[1] * 4
                    + cuit_num[2] * 3
                    + cuit_num[3] * 2
                    + cuit_num[4] * 7
                    + cuit_num[5] * 6
                    + cuit_num[6] * 5
                    + cuit_num[7] * 4
                    + cuit_num[8] * 3
                    + cuit_num[9] * 2
                )
                % 11
            )
            if verif == cuit_num[-1]:
                if str(cuitf.get())[2] != "-":
                    data = (
                        str(cuitf.get())[0]
                        + str(cuitf.get())[1]
                        + "-"
                        + str(cuitf.get())[2]
                        + str(cuitf.get())[3]
                        + str(cuitf.get())[4]
                        + str(cuitf.get())[5]
                        + str(cuitf.get())[6]
                        + str(cuitf.get())[7]
                        + str(cuitf.get())[8]
                        + str(cuitf.get())[9]
                        + "-"
                        + str(cuitf.get())[10],
                        razonsocialf.get(),
                        numerodefacturaf.get(),
                        fechaf.get_date(),
                        preciof.get(),
                        cantidadf.get(),
                        alicuotaf.get(),
                        compraventaf.get(),
                    )
                else:
                    data = (
                        cuitf.get(),
                        razonsocialf.get(),
                        numerodefacturaf.get(),
                        fechaf.get_date(),
                        preciof.get(),
                        cantidadf.get(),
                        alicuotaf.get(),
                        compraventaf.get(),
                    )
                # db.connect()
                factura_alta = Facturas.create(
                    CUIT=data[0],
                    RazonSocial=data[1],
                    Numero_de_factura=data[2],
                    Fecha=data[3],
                    Precio=data[4],
                    Cantidad=data[5],
                    Alicuota=data[6],
                    Impuesto=Facturas.gs_impuesto(),
                    Neto=Facturas.gs_neto(),
                    Total=Facturas.gs_total(),
                    Compra_Venta=data[7],
                )
                factura_alta.save()
                db.close()
                showinfo(
                    "Registro dado de alta",
                    "Se cargó la factura N°: " + str(numerodefacturaf.get()),
                )
                cuitf.set(""),
                razonsocialf.set(""),
                numerodefacturaf.set(0),
                fechaf.set_date(datetime.date.today()),
                preciof.set(0),
                cantidadf.set(0),
                alicuotaf.set(0),
                compraventaf.set("")
                self_a.actualizar_treeview(arbol)
            else:
                try:
                    raise (
                        ExceptionOwn(
                            "Error en formato de CUIT",
                            "Ingrese un CUIT valido con formato 'XX-XXXXXXXX-X' o 'XXXXXXXXXXX'.",
                        )
                    )
                except ExceptionOwn as error:
                    showerror(
                        error.msj_1,
                        error.msj_2,
                    )
        else:
            try:
                raise (
                    ExceptionOwn(
                        "Error en formato de CUIT",
                        "Ingrese un CUIT valido con formato 'XX-XXXXXXXX-X' o 'XXXXXXXXXXX'.",
                    )
                )
            except ExceptionOwn as error:
                showerror(
                    error.msj_1,
                    error.msj_2,
                )

    # La funcion de actualizacion del treeview:
    def actualizar_treeview(self_at, el_treeview):
        records = el_treeview.get_children()
        for element in records:
            el_treeview.delete(element)

        query = factura_consulta.select().dicts()
        for fila in query:
            print(str(list(fila.values())[4]))

            el_treeview.insert(
                "",
                0,
                text=list(fila.values())[0],
                values=(
                    list(fila.values())[1],
                    list(fila.values())[2],
                    list(fila.values())[3],
                    str(list(fila.values())[4]),
                    "${:,.2f}".format(list(fila.values())[5]),
                    list(fila.values())[6],
                    list(fila.values())[7],
                    "${:,.2f}".format(list(fila.values())[8]),
                    "${:,.2f}".format(list(fila.values())[9]),
                    "${:,.2f}".format(list(fila.values())[10]),
                    list(fila.values())[11],
                ),
            )

    # La funcion para borrar las lineas seleccionadas:
    def fborrar(self_bor, mi_tree):
        valor = mi_tree.selection()
        # print(valor)  # ('I005',)
        for x in range(0, len(valor)):
            item = mi_tree.item(valor[x])
            mi_id = item["text"]
            print(item["text"])
            query = Facturas.delete().where(Facturas.id == mi_id)
            query.execute()
        self_bor.actualizar_treeview(mi_tree)

    # Funcion para seleccionar lo que voy a modificar
    def modificar(
        self_mod,
        cuitf,
        razonsocialf,
        numerodefacturaf,
        fechaf,
        preciof,
        cantidadf,
        alicuotaf,
        compraventaf,
        mi_tree,
    ):
        cuitf.delete(0, END)
        razonsocialf.delete(0, END)
        numerodefacturaf.delete(0, END)
        preciof.delete(0, END)
        cantidadf.delete(0, END)
        alicuotaf.delete(0, END)
        compraventaf.delete(0, END)
        a_modificar = mi_tree.focus()
        valores = mi_tree.item(a_modificar, "values")
        fechu = valores[3]
        fechux = (
            fechu[5]
            + fechu[6]
            + "/"
            + fechu[-2]
            + fechu[-1]
            + "/"
            + fechu[2]
            + fechu[3]
        )
        cuitf.insert(0, valores[0])
        razonsocialf.insert(0, valores[1])
        numerodefacturaf.insert(0, valores[2])
        fechaf.set_date(fechux)
        preciof.insert(0, str(str(valores[4])[1:]).replace(",", ""))
        cantidadf.insert(0, valores[5])
        alicuotaf.insert(0, valores[6])
        compraventaf.insert(0, valores[10])

    # Funcion para guardar la modificacion ingresada
    def guardar_modificacion(
        self_gm,
        cuitf,
        razonsocialf,
        numerodefacturaf,
        fechaf,
        preciof,
        cantidadf,
        alicuotaf,
        compraventaf,
        mi_tree,
    ):
        validation = ValidadorRegex(cuitf.get())

        if validation.validator():
            cuit_str = str(cuitf.get())
            cuit_num = [int(x) for x in cuit_str if x != "-"]
            verif = 11 - (
                (
                    cuit_num[0] * 5
                    + cuit_num[1] * 4
                    + cuit_num[2] * 3
                    + cuit_num[3] * 2
                    + cuit_num[4] * 7
                    + cuit_num[5] * 6
                    + cuit_num[6] * 5
                    + cuit_num[7] * 4
                    + cuit_num[8] * 3
                    + cuit_num[9] * 2
                )
                % 11
            )
            if verif == cuit_num[-1]:
                a_modificar = mi_tree.focus()

                if str(cuitf.get())[2] != "-":
                    data = (
                        str(cuitf.get())[0]
                        + str(cuitf.get())[1]
                        + "-"
                        + str(cuitf.get())[2]
                        + str(cuitf.get())[3]
                        + str(cuitf.get())[4]
                        + str(cuitf.get())[5]
                        + str(cuitf.get())[6]
                        + str(cuitf.get())[7]
                        + str(cuitf.get())[8]
                        + str(cuitf.get())[9]
                        + "-"
                        + str(cuitf.get())[10],
                        razonsocialf.get(),
                        numerodefacturaf.get(),
                        fechaf.get_date(),
                        preciof.get(),
                        cantidadf.get(),
                        alicuotaf.get(),
                        compraventaf.get(),
                        mi_tree.item(a_modificar)["text"],
                    )
                else:
                    data = (
                        cuitf.get(),
                        razonsocialf.get(),
                        numerodefacturaf.get(),
                        fechaf.get_date(),
                        preciof.get(),
                        cantidadf.get(),
                        alicuotaf.get(),
                        compraventaf.get(),
                        mi_tree.item(a_modificar)["text"],
                    )

                query = Facturas.update(
                    CUIT=data[0],
                    RazonSocial=data[1],
                    Numero_de_factura=data[2],
                    Fecha=str(data[3]),
                    Precio=data[4],
                    Cantidad=data[5],
                    Alicuota=data[6],
                ).where(Facturas.id == data[8])
                query.execute()

                query = Facturas.update(
                    Impuesto=Facturas.gs_impuesto(),
                    Neto=Facturas.gs_neto(),
                    Total=Facturas.gs_total(),
                    Compra_Venta=data[7],
                ).where(Facturas.id == data[8])
                query.execute()

                print("Estoy en alta todo ok")
                self_gm.actualizar_treeview(mi_tree)
            else:
                showerror(
                    "Error en formato de CUIT",
                    "Ingrese un CUIT válido con formato ##-########-# o ###########",
                )
        else:
            showerror(
                "Error en formato de CUIT",
                "Ingrese un CUIT válido con formato ##-########-# o ###########",
            )
