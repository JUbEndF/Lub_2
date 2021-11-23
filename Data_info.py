import re

class Data:
    info: dict

    def __init__(self, line: dict):
        self.info = line.copy()

    def check_number(self, name: str, size: int) -> bool:
        if re.match(r'\d{size}', self.info[name]):
            return False
        return True

    def check_email(self) -> bool:

        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, self.info.get("email")):
            return True
        return False

    def check_weight(self) -> bool:
        if isinstance(self.info.get("weight"), int):
            if 30 < self.info.get("weight") < 460:
                return True
        return False

    def check_snils(self) -> bool:
        return self.check_number("snils", 11)

    def check_passport_series(self) -> bool:
        return self.check_number("passport_series", 4)

    def check_university(self) -> bool:
        pattern = '([Уу]ниверситет|[Aа]кадем| [Ии]нститут|им. |[Пп]олитех|([А-Я]{3,}))+(\s|[а-я])'
        if re.match(pattern, self.info["university"]) is not None:
            return True
        else:
            return False

    def check_age(self) -> bool:
        if isinstance(self.info.get("age"), int):
            if 17 < self.info["age"] < 90:
                return True
        return False

    def check_academic_degree(self) -> bool:
        if re.match('Бакалавр|Специалист|Магистр|Кандидат наук|Доктор наук', self.info["academic_degree"]):
            return True
        return False


    def check_worldview(self) -> bool:
        if re.match('Христианство|Ислам|Буддизм|Иудаизм|Индуизм|Сикхизм|Конфуцианство|Даосизм|Джайнизм|Синтоизм', self.info["worldview"]):
            return True
        return False

    def check_address(self) -> bool:
        pattern = '(([Аа]ллея)|([Уу]лица)|(ул.))((([А-яёЁ ]?)+)?)([ А-Я. ]*)(\d+)'
        if re.match(pattern, self.info['address']):
            return True
        else:
            return False
