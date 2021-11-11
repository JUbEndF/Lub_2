import re

class Data:
    info: dict

    def __init__(self, line: str):
        self.info = {
            "email": line[0],
            "weight": line[1],
            "snils": line[2],
            "passport_series": line[3],
            "university": line[4],
            "age": line[5],
            "academic_degree": line[6],
            "worldview": line[7],
            "address": line[8]
        }

    def check_email(self) -> bool:

        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, self.info.get("email")):
            return True
        return False

    def check_number(self, name: str, size: int) -> bool:
        if re.match(r'\d{size}', self.info[name]):
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