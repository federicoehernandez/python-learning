"""
Modulo valida_regex:
    En este modulo se encuentra la validacion realizada por **Regex** que se utiliza en el ***modulo_abm***.
"""
import re


class ValidadorRegex:
    def __init__(self, character_chain):
        self.patron = re.compile(r"^(20|23|27|30|33)([0-9]{9}|-[0-9]{8}-[0-9]{1})$")
        self.character_chain = character_chain

    def validator(self):
        """
        El metodo **validator** se encarga de comprobar si el string ingresado en la instanciacion de la clase coincide con el codigo regex utilizado.
        """
        if self.patron.match(self.character_chain):
            return True
        else:
            return False
