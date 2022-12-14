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


class Vista:

    # Defino la ventana principal de la aplicación:
    # root = Tk()

    def __init__(self, root):
        self.operaciones_abm = Abm()
        self.consultas_cons = Consultas()
        self.opciones_opc = Opciones()
        # Defino las variables que voy a usar en tkinter:
        self.cuit = StringVar()
        self.razon_social = StringVar()
        self.numero_factura = IntVar()
        self.fecha = StringVar()
        self.precio = DoubleVar()
        self.cantidad = IntVar()
        self.alicuota = IntVar()
        self.impuesto = IntVar()
        self.neto = IntVar()
        self.total = IntVar()

        self.eleccion_color = StringVar()

        # Fijo el tamaño de la ventana y el título:
        root.resizable(width=False, height=False)
        root.title("Base de datos de Facturas de compra y venta")

        # Creo las etiquetas:
        self.l_ingreso_datos = ttk.Label(root, text="INGRESO DE DATOS")
        self.l_abm = ttk.Label(root, text="ABM")
        self.l_listar = ttk.Label(root, text="LISTAR")
        self.l_opciones = ttk.Label(root, text="OPCIONES")
        self.l_cuit = ttk.Label(root, text="CUIT")
        self.l_razon_social = ttk.Label(root, text="Razon social")
        self.l_numero_factura = ttk.Label(root, text="Numero de factura")
        self.l_fecha = ttk.Label(root, text="Fecha")
        self.l_precio = ttk.Label(root, text="Precio")
        self.l_cantidad = ttk.Label(root, text="Cantidad")
        self.l_alicuota = ttk.Label(root, text="Alicuota")
        self.l_compra_venta = ttk.Label(root, text="Compra/Venta")
        self.l_lista_registros = ttk.Label(root, text="LISTA DE FACTURAS")
        self.l_elegir_cuit = ttk.Label(root, text="Seleccionar CUIT")

        # Creo los campos para ingresar la informacion
        self.e_text1 = ttk.Entry(root, textvariable=self.cuit, width=15)
        self.e_text2 = ttk.Entry(root, textvariable=self.razon_social, width=15)
        self.e_text3 = ttk.Entry(root, textvariable=self.numero_factura, width=15)
        self.combobox_1 = ttk.Combobox(root, width=12)
        self.combobox_1["values"] = ("Compra", "Venta")
        self.e_text5 = ttk.Entry(root, textvariable=self.precio, width=15)
        self.e_text6 = ttk.Entry(root, textvariable=self.cantidad, width=15)
        self.e_text7 = ttk.Entry(root, textvariable=self.alicuota, width=15)
        self.c_fecha = DateEntry(root, width=12)

        # Creo los botones
        self.b_agregar = ttk.Button(
            root,
            text="Agregar",
            command=lambda: self.operaciones_abm.alta2(
                self.cuit,
                self.razon_social,
                self.numero_factura,
                self.c_fecha,
                self.precio,
                self.cantidad,
                self.alicuota,
                self.combobox_1,
                self.tree,
            ),
        )
        self.b_borrar = ttk.Button(
            root,
            text="Borrar",
            command=lambda: self.operaciones_abm.fborrar(self.tree),
        )
        self.b_salir = ttk.Button(
            root, text="Salir", command=lambda: self.opciones_opc.salir(root)
        )
        self.b_ver = ttk.Button(
            root,
            text="Ver seleccionado",
            width=15,
            command=lambda: self.consultas_cons.fver(self.tree),
        )
        self.b_modificar = ttk.Button(
            root,
            text="Guardar modificacion",
            command=lambda: self.operaciones_abm.guardar_modificacion(
                self.cuit,
                self.razon_social,
                self.numero_factura,
                self.c_fecha,
                self.precio,
                self.cantidad,
                self.alicuota,
                self.combobox_1,
                self.tree,
            ),
        )
        self.b_selec_modif = ttk.Button(
            root,
            text="Seleccionar para modificar",
            command=lambda: self.operaciones_abm.modificar(
                self.e_text1,
                self.e_text2,
                self.e_text3,
                self.c_fecha,
                self.e_text5,
                self.e_text6,
                self.e_text7,
                self.combobox_1,
                self.tree,
            ),
        )

        self.b_listar_c = ttk.Button(
            root,
            text="Listar compras",
            width=15,
            command=lambda: self.consultas_cons.listar_c(self.tree),
        )
        self.b_listar_v = ttk.Button(
            root,
            text="Listar ventas",
            width=15,
            command=lambda: self.consultas_cons.listar_v(self.tree),
        )
        self.b_elegir_color = ttk.Button(
            root,
            text="Elegir color",
            command=lambda: self.opciones_opc.elegir_color(root),
        )
        self.b_select_all = ttk.Button(
            root,
            text="Seleccionar todo",
            width=15,
            command=lambda: self.consultas_cons.select_all(self.tree),
        )

        self.b_selec_cuit = ttk.Combobox(
            root,
            width=15,
            postcommand=lambda: self.consultas_cons.updtcblist(self.b_selec_cuit),
        )
        self.b_selec_cuit["values"] = self.consultas_cons.traer_lista()

        self.b_ver_saldo = ttk.Button(
            root,
            width=15,
            text="Mostrar saldo",
            command=lambda: self.consultas_cons.ver_saldo(self.b_selec_cuit),
        )

        self.treeScroll = ttk.Scrollbar(root)

        # Creo el Treeview
        self.tree = ttk.Treeview(root)

        self.tree["columns"] = (
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
        self.tree.column("#0", width=50, minwidth=50, anchor=W)
        self.tree.column("col1", width=100, minwidth=80, anchor=CENTER)
        self.tree.column("col2", width=80, minwidth=80)
        self.tree.column("col3", width=120, minwidth=100)
        self.tree.column("col4", width=100, minwidth=100, anchor=CENTER)
        self.tree.column("col5", width=100, minwidth=100)
        self.tree.column("col6", width=100, minwidth=100, anchor=CENTER)
        self.tree.column("col7", width=100, minwidth=100)
        self.tree.column("col8", width=100, minwidth=100)
        self.tree.column("col9", width=100, minwidth=100)
        self.tree.column("col10", width=100, minwidth=100)
        self.tree.column("col11", width=100, minwidth=100, anchor=CENTER)

        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="CUIT")
        self.tree.heading("col2", text="Razon social")
        self.tree.heading("col3", text="Numero de factura")
        self.tree.heading("col4", text="Fecha")
        self.tree.heading("col5", text="Precio")
        self.tree.heading("col6", text="Cantidad")
        self.tree.heading("col7", text="Alicuota %")
        self.tree.heading("col8", text="Impuesto")
        self.tree.heading("col9", text="Neto")
        self.tree.heading("col10", text="Total")
        self.tree.heading("col11", text="Compra/venta")
        self.tree.configure(yscrollcommand=self.treeScroll.set)
        self.tree["yscrollcommand"] = self.treeScroll.set
        self.treeScroll.configure(command=self.tree.yview)

        # Traigo los registros que estan en este momento en la base al Treeview (en caso que haya registros antes de ejecutar el programa):

        resultado = Facturas.select().dicts()

        for fila in resultado:
            self.tree.insert(
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
        self.l_ingreso_datos.grid(column=0, row=0)
        self.l_abm.grid(column=2, row=0)
        self.l_listar.grid(column=3, row=0)
        self.l_opciones.grid(column=4, row=0)
        self.l_cuit.grid(column=0, row=1)
        self.l_razon_social.grid(column=0, row=2)
        self.l_numero_factura.grid(column=0, row=3)
        self.l_fecha.grid(column=0, row=4)
        self.l_precio.grid(column=0, row=5)
        self.l_cantidad.grid(column=0, row=6)
        self.l_alicuota.grid(column=0, row=7)
        self.l_compra_venta.grid(column=0, row=8)
        self.l_lista_registros.grid(column=0, row=9, columnspan=11)

        self.e_text1.grid(column=1, row=1)
        self.e_text2.grid(column=1, row=2)
        self.e_text3.grid(column=1, row=3)

        self.e_text5.grid(column=1, row=5)
        self.e_text6.grid(column=1, row=6)
        self.e_text7.grid(column=1, row=7)

        self.tree.grid(column=0, row=10, columnspan=12)

        self.b_agregar.grid(column=2, row=1)
        self.b_borrar.grid(column=2, row=2)
        self.b_selec_modif.grid(column=2, row=3)
        self.b_modificar.grid(column=2, row=4)
        self.b_ver.grid(column=3, row=3)
        self.b_listar_c.grid(column=3, row=1)
        self.b_listar_v.grid(column=3, row=2)
        self.b_select_all.grid(column=3, row=4)
        self.b_ver_saldo.grid(column=3, row=7)

        self.c_fecha.grid(column=1, row=4)

        self.b_salir.grid(column=4, row=2)
        self.b_elegir_color.grid(column=4, row=1)

        self.combobox_1.grid(column=1, row=8)

        self.b_selec_cuit.grid(column=3, row=6)

        self.l_elegir_cuit.grid(column=3, row=5)

        self.treeScroll.grid(column=12, row=10, sticky=tk.NS)

    # mainloop()
