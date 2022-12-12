class ExceptionOwn(Exception):
    def __init__(self, *args):
        self.msj_1 = args[0]
        self.msj_2 = args[1]
