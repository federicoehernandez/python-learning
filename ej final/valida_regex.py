import re


class ValidadorRegex:
    def __init__(self, character_chain):
        self.patron = re.compile(r"^(20|23|27|30|33)([0-9]{9}|-[0-9]{8}-[0-9]{1})$")
        self.character_chain = character_chain

    def validator(self):
        if self.patron.match(self.character_chain):
            return True
        else:
            return False


# validation = ValidadorRegex("30-70836728-8")
# validation.validator()
