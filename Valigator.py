import re
class Validator:


    def __init__(self, text: str) -> None:


    def check_email(self, email: str) -> bool:

        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, email):
            return True
        return False

    def check_number(self, number: str, size: int) -> bool:
        if range(str) != size | number.isdigit():
            return False
        return True

    def check_float(self, number: str) -> bool:
        try:
            float(number)
            return True
        except ValueError:
            return False

    def check_weight(self, m: str) -> bool:
        if self.check_float(m) & float(m) > 30 & float(m) < 460:
            return True
        return False