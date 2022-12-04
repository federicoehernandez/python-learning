from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
from tkcalendar import DateEntry
import tkinter as tk
from tkinter.messagebox import *
from modulo_abm import Abm
from modulo_consultas import Consultas
from modulo_opciones import Opciones
from modulo_abm import Facturas

"""
try:
    mabm.conexion()
    mabm.crear_tabla()
    print("Se creo la base 'Facturas de compra y venta'")

except:

    print(
        "Ya está creada la base 'Facturas de compra y venta', se muestran los registros actuales"
    )
"""


class Vista:

    # Defino la ventana principal de la aplicación:
    # root = Tk()

    def __init__(self_ivista, root):
        self_ivista.operaciones_abm = Abm()
        self_ivista.consultas_cons = Consultas()
        self_ivista.opciones_opc = Opciones()
        # Defino las variables que voy a usar en tkinter:
        self_ivista.cuit = StringVar()
        self_ivista.razon_social = StringVar()
        self_ivista.numero_factura = IntVar()
        self_ivista.fecha = StringVar()
        self_ivista.precio = DoubleVar()
        self_ivista.cantidad = IntVar()
        self_ivista.alicuota = IntVar()
        self_ivista.impuesto = IntVar()
        self_ivista.neto = IntVar()
        self_ivista.total = IntVar()

        self_ivista.eleccion_color = StringVar()

        # Fijo el tamaño de la ventana y el título:
        root.resizable(width=False, height=False)
        root.title("Base de datos de Facturas de compra y venta")

        # Creo las etiquetas:
        self_ivista.l_ingreso_datos = ttk.Label(root, text="INGRESO DE DATOS")
        self_ivista.l_abm = ttk.Label(root, text="ABM")
        self_ivista.l_listar = ttk.Label(root, text="LISTAR")
        self_ivista.l_opciones = ttk.Label(root, text="OPCIONES")
        self_ivista.l_cuit = ttk.Label(root, text="CUIT")
        self_ivista.l_razon_social = ttk.Label(root, text="Razon social")
        self_ivista.l_numero_factura = ttk.Label(root, text="Numero de factura")
        self_ivista.l_fecha = ttk.Label(root, text="Fecha")
        self_ivista.l_precio = ttk.Label(root, text="Precio")
        self_ivista.l_cantidad = ttk.Label(root, text="Cantidad")
        self_ivista.l_alicuota = ttk.Label(root, text="Alicuota")
        self_ivista.l_compra_venta = ttk.Label(root, text="Compra/Venta")
        self_ivista.l_lista_registros = ttk.Label(root, text="LISTA DE FACTURAS")
        self_ivista.l_elegir_cuit = ttk.Label(root, text="Seleccionar CUIT")

        # Creo los campos para ingresar la informacion
        self_ivista.e_text1 = ttk.Entry(root, textvariable=self_ivista.cuit, width=15)
        self_ivista.e_text2 = ttk.Entry(
            root, textvariable=self_ivista.razon_social, width=15
        )
        self_ivista.e_text3 = ttk.Entry(
            root, textvariable=self_ivista.numero_factura, width=15
        )
        self_ivista.combobox_1 = ttk.Combobox(root, width=12)
        self_ivista.combobox_1["values"] = ("Compra", "Venta")
        self_ivista.e_text5 = ttk.Entry(root, textvariable=self_ivista.precio, width=15)
        self_ivista.e_text6 = ttk.Entry(
            root, textvariable=self_ivista.cantidad, width=15
        )
        self_ivista.e_text7 = ttk.Entry(
            root, textvariable=self_ivista.alicuota, width=15
        )
        self_ivista.c_fecha = DateEntry(root, width=12)

        # Creo los botones
        self_ivista.b_agregar = ttk.Button(
            root,
            text="Agregar",
            command=lambda: self_ivista.operaciones_abm.alta2(
                self_ivista.cuit,
                self_ivista.razon_social,
                self_ivista.numero_factura,
                self_ivista.c_fecha,
                self_ivista.precio,
                self_ivista.cantidad,
                self_ivista.alicuota,
                self_ivista.combobox_1,
                self_ivista.tree,
            ),
        )
        self_ivista.b_borrar = ttk.Button(
            root,
            text="Borrar",
            command=lambda: self_ivista.operaciones_abm.fborrar(self_ivista.tree),
        )
        self_ivista.b_salir = ttk.Button(
            root, text="Salir", command=lambda: self_ivista.opciones_opc.salir(root)
        )
        self_ivista.b_ver = ttk.Button(
            root,
            text="Ver seleccionado",
            width=15,
            command=lambda: self_ivista.consultas_cons.fver(self_ivista.tree),
        )
        self_ivista.b_modificar = ttk.Button(
            root,
            text="Guardar modificacion",
            command=lambda: self_ivista.operaciones_abm.guardar_modificacion(
                self_ivista.cuit,
                self_ivista.razon_social,
                self_ivista.numero_factura,
                self_ivista.c_fecha,
                self_ivista.precio,
                self_ivista.cantidad,
                self_ivista.alicuota,
                self_ivista.combobox_1,
                self_ivista.tree,
            ),
        )
        self_ivista.b_selec_modif = ttk.Button(
            root,
            text="Seleccionar para modificar",
            command=lambda: self_ivista.operaciones_abm.modificar(
                self_ivista.e_text1,
                self_ivista.e_text2,
                self_ivista.e_text3,
                self_ivista.c_fecha,
                self_ivista.e_text5,
                self_ivista.e_text6,
                self_ivista.e_text7,
                self_ivista.combobox_1,
                self_ivista.tree,
            ),
        )

        self_ivista.b_listar_c = ttk.Button(
            root,
            text="Listar compras",
            width=15,
            command=lambda: self_ivista.consultas_cons.listar_c(self_ivista.tree),
        )
        self_ivista.b_listar_v = ttk.Button(
            root,
            text="Listar ventas",
            width=15,
            command=lambda: self_ivista.consultas_cons.listar_v(self_ivista.tree),
        )
        self_ivista.b_elegir_color = ttk.Button(
            root,
            text="Elegir color",
            command=lambda: self_ivista.opciones_opc.elegir_color(root),
        )
        self_ivista.b_select_all = ttk.Button(
            root,
            text="Seleccionar todo",
            width=15,
            command=lambda: self_ivista.consultas_cons.select_all(self_ivista.tree),
        )

        self_ivista.b_selec_cuit = ttk.Combobox(
            root,
            width=15,
            postcommand=lambda: self_ivista.consultas_cons.updtcblist(
                self_ivista.b_selec_cuit
            ),
        )
        self_ivista.b_selec_cuit["values"] = self_ivista.consultas_cons.traer_lista()

        self_ivista.b_ver_saldo = ttk.Button(
            root,
            width=15,
            text="Mostrar saldo",
            command=lambda: self_ivista.consultas_cons.ver_saldo(
                self_ivista.b_selec_cuit
            ),
        )

        self_ivista.treeScroll = ttk.Scrollbar(root)

        # Creo el Treeview
        self_ivista.tree = ttk.Treeview(root)

        self_ivista.tree["columns"] = (
            "col1",
            "col2",
            "col3",
            "col4",
            "col5",
            "col6",
            "col7",
            "col8",
            "col9",
            "col10",
            "col11",
        )
        self_ivista.tree.column("#0", width=50, minwidth=50, anchor=W)
        self_ivista.tree.column("col1", width=100, minwidth=80, anchor=CENTER)
        self_ivista.tree.column("col2", width=80, minwidth=80)
        self_ivista.tree.column("col3", width=120, minwidth=100)
        self_ivista.tree.column("col4", width=100, minwidth=100, anchor=CENTER)
        self_ivista.tree.column("col5", width=100, minwidth=100)
        self_ivista.tree.column("col6", width=100, minwidth=100, anchor=CENTER)
        self_ivista.tree.column("col7", width=100, minwidth=100)
        self_ivista.tree.column("col8", width=100, minwidth=100)
        self_ivista.tree.column("col9", width=100, minwidth=100)
        self_ivista.tree.column("col10", width=100, minwidth=100)
        self_ivista.tree.column("col11", width=100, minwidth=100, anchor=CENTER)

        self_ivista.tree.heading("#0", text="ID")
        self_ivista.tree.heading("col1", text="CUIT")
        self_ivista.tree.heading("col2", text="Razon social")
        self_ivista.tree.heading("col3", text="Numero de factura")
        self_ivista.tree.heading("col4", text="Fecha")
        self_ivista.tree.heading("col5", text="Precio")
        self_ivista.tree.heading("col6", text="Cantidad")
        self_ivista.tree.heading("col7", text="Alicuota %")
        self_ivista.tree.heading("col8", text="Impuesto")
        self_ivista.tree.heading("col9", text="Neto")
        self_ivista.tree.heading("col10", text="Total")
        self_ivista.tree.heading("col11", text="Compra/venta")
        self_ivista.tree.configure(yscrollcommand=self_ivista.treeScroll.set)
        self_ivista.tree["yscrollcommand"] = self_ivista.treeScroll.set
        self_ivista.treeScroll.configure(command=self_ivista.tree.yview)

        # Traigo los registros que estan en este momento en la base al Treeview (en caso que haya registros antes de ejecutar el programa):

        resultado = Facturas.select().dicts()

        for fila in resultado:
            self_ivista.tree.insert(
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

        # Posiciono las etiquetas, botones y campos de entrada
        self_ivista.l_ingreso_datos.grid(column=0, row=0)
        self_ivista.l_abm.grid(column=2, row=0)
        self_ivista.l_listar.grid(column=3, row=0)
        self_ivista.l_opciones.grid(column=4, row=0)
        self_ivista.l_cuit.grid(column=0, row=1)
        self_ivista.l_razon_social.grid(column=0, row=2)
        self_ivista.l_numero_factura.grid(column=0, row=3)
        self_ivista.l_fecha.grid(column=0, row=4)
        self_ivista.l_precio.grid(column=0, row=5)
        self_ivista.l_cantidad.grid(column=0, row=6)
        self_ivista.l_alicuota.grid(column=0, row=7)
        self_ivista.l_compra_venta.grid(column=0, row=8)
        self_ivista.l_lista_registros.grid(column=0, row=9, columnspan=11)

        self_ivista.e_text1.grid(column=1, row=1)
        self_ivista.e_text2.grid(column=1, row=2)
        self_ivista.e_text3.grid(column=1, row=3)

        self_ivista.e_text5.grid(column=1, row=5)
        self_ivista.e_text6.grid(column=1, row=6)
        self_ivista.e_text7.grid(column=1, row=7)

        self_ivista.tree.grid(column=0, row=10, columnspan=12)

        self_ivista.b_agregar.grid(column=2, row=1)
        self_ivista.b_borrar.grid(column=2, row=2)
        self_ivista.b_selec_modif.grid(column=2, row=3)
        self_ivista.b_modificar.grid(column=2, row=4)
        self_ivista.b_ver.grid(column=3, row=3)
        self_ivista.b_listar_c.grid(column=3, row=1)
        self_ivista.b_listar_v.grid(column=3, row=2)
        self_ivista.b_select_all.grid(column=3, row=4)
        self_ivista.b_ver_saldo.grid(column=3, row=7)

        self_ivista.c_fecha.grid(column=1, row=4)

        self_ivista.b_salir.grid(column=4, row=2)
        self_ivista.b_elegir_color.grid(column=4, row=1)

        self_ivista.combobox_1.grid(column=1, row=8)

        self_ivista.b_selec_cuit.grid(column=3, row=6)

        self_ivista.l_elegir_cuit.grid(column=3, row=5)

        self_ivista.treeScroll.grid(column=12, row=10, sticky=tk.NS)

    # mainloop()
