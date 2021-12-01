import re

class Data:
    '''Класс единичного словаря данных'''
    _info: dict

    def __init__(self, line: dict):
        self._info = line.copy()

    def check_valid(self) -> bool:
        if self.check_email() and self.check_age() and self.check_snils() and self.check_academic_degree() and self.check_passport_series() and self.check_address() and self.check_weight() and self.check_university() and self.check_worldview():
            return True
        return False


    def info(self) -> dict:
        return self._info.copy()

    def check_number(self, name: str, size: int) -> bool:
        pattern = "\d{size}"
        if re.match(pattern, self._info[name]):
            return False
        return True

    def check_email(self) -> bool:

        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, self._info.get("email")):
            return True
        return False

    def check_weight(self) -> bool:
        if isinstance(self._info.get("weight"), int):
            if 30 < self._info.get("weight") < 460:
                return True
        return False

    def check_snils(self) -> bool:
        return self.check_number("snils", 11)

    def check_passport_series(self) -> bool:
        pattern = "[\d{2}\s]"
        if re.match(pattern, self._info["passport_series"]):
            return True
        return False

    def check_university(self) -> bool:
        pattern = '([Уу]ниверситет|[Aа]кадем|[Ии]нститут|им.|[Пп]олитех|([А-Я]{3,}))+(\s|[а-я])'
        if re.match(pattern, self._info["university"]):
            return True
        else:
            return False

    def check_age(self) -> bool:
        if isinstance(self._info.get("age"), int):
            if 17 < self._info["age"] < 90:
                return True
        return False

    def check_academic_degree(self) -> bool:
        if re.match('Бакалавр|Специалист|Магистр|Кандидат наук|Доктор наук', self._info["academic_degree"]):
            return True
        return False


    def check_worldview(self) -> bool:
        if re.match('Христианство|Ислам|Буддизм|Иудаизм|Индуизм|Сикхизм|Конфуцианство|Даосизм|Джайнизм|Синтоизм', self._info["worldview"]):
            return True
        return False

    def check_address(self) -> bool:
        pattern = '(([Аа]ллея)|([Уу]лица)|(ул.))((([А-яёЁ ]?)+)?)([ А-Я. ]*)(\d+)'
        if re.match(pattern, self._info['address']):
            return True
        else:
            return False
