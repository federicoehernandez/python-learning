class ExceptionOwn(Exception):
    def mensaje_de_error(self):
        msg = "Ingrese un CUIT valido con formato 'XX-XXXXXXXX-X' o 'XXXXXXXXXXX'."
        return msg

def prueba():
    

try
x = -1

if x < 0:
    raise ExceptionOwn as eo