from peewee import *
from inst_db_orm2 import factura_consulta
from inst_db_orm2 import Facturas
from inst_db_orm2 import db

# query = factura_consulta.select().where(factura_consulta.id > 0)

# for factura in factura_consulta.select():
#    print(factura.CUIT)

# query = factura_consulta.select().dicts()
# for fila in query:
#    print(fila[0])

# for x in query:
#    print(str(list(x.values())[4]))

# query = Facturas.delete().where(Facturas.id == 39)
# query.execute()


"""query = Facturas.update(
    CUIT="30-70836728-8",
    RazonSocial="SociedadX",
    Numero_de_factura=987,
    Fecha="2022-12-01",
    Precio=200,
    Cantidad=1,
    Alicuota=1,
).where(Facturas.id == 8)
query.execute()

query = Facturas.update(
    Impuesto=Facturas.gs_impuesto(),
    Neto=Facturas.gs_neto(),
    Total=Facturas.gs_total(),
    Compra_Venta="Compra",
).where(Facturas.id == 8)
query.execute()"""


"""factura_generica = Facturas.create(
    CUIT="30-70836728-8",
    RazonSocial="tuplas[1]",
    Numero_de_factura=456789,
    Fecha="2022-11-26",
    Precio=124.60,
    Cantidad=2,
    Alicuota=1.5,
    Impuesto=Facturas.gs_impuesto(),
    Neto=Facturas.gs_neto(),
    Total=Facturas.gs_total(),
    Compra_Venta="Compra",
)
factura_generica.save()"""
