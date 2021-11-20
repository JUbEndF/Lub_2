import re

class Data:
    info: dict

    def __init__(self, line: str):
        self.info = {
            "email": line[0],#+
            "weight": line[1],#+
            "snils": line[2],#+
            "passport_series": line[3],#+
            "university": line[4],#+
            "age": line[5],#+
            "academic_degree": line[6],#+
            "worldview": line[7],#+
            "address": line[8]#
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

    def chech_age(self) -> bool:
        if  17 < int(self.info[5])& int(self.info[5]) < 65:
            return True
        return False

    def check_snils(self) -> bool:
        return self.check_number("snils", 11)
    def check_passport_series(self) -> bool:
        return self.check_number("passport_series", 4)

    def check_worldview(self) -> bool:
        return re.findall(self.info[7], "христианство,ислам,буддизм,иудаизм,индуизм,сикхизм,конфуцианство,даосизм,джайнизм,синтоизм") == self.info[7]

    def check_worldview(self) -> bool:
        return re.findall(self.info[7], "бакалавриат,специалист,магистратр,кандидат наук, доктор наук") == self.info[6]

    def check_university(self) -> bool:
        pattern = '([Уу]ниверситет|[Aа]кадем| [Ии]нститут|им. |[Пп]олитех|([А-Я]{3,}))+(\s|[а-я])'
        if re.match(pattern, self.info[4]) is not None:
            return True
        else:
            return False

    def check_address(self) -> bool:
        pattern = '(([Аа]ллея)|([Уу]лица)|(ул.))((([А-яёЁ ]?)+)?)([ А-Я. ]*)(\d+)'
        if re.match(pattern, self.info[8]) is not None:
            return True
        else:
            return False