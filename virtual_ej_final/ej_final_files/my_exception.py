"""
Modulo my_exception:
    Este modulo contiene el manejo de excepciones que es utilizado en el modulo_abm.
"""


class ExceptionOwn(Exception):
    """
    La clase **ExceptionOwn** est creada en base a la clase padre **Exception** y al producirse un error definido devuelve los mensajes de advertencia al usuario.
    """

    def __init__(self, msj_1, msj_2):
        self.msj_1 = msj_1
        self.msj_2 = msj_2


# self.msj = "Ingrese un CUIT valido con formato 'XX-XXXXXXXX-X' o 'XXXXXXXXXXX'."
