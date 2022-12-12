class ExceptionOwn(Exception):
    def __init__(self, msj_1, msj_2):
        self.msj_1 = msj_1
        self.msj_2 = msj_2


# self.msj = "Ingrese un CUIT valido con formato 'XX-XXXXXXXX-X' o 'XXXXXXXXXXX'."
