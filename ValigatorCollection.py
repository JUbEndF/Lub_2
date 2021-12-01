from Data_info import Data
from tqdm import tqdm

class Validator_list:
    _array: list

    def __init__(self, array: list) -> None:
        """Конструктор класса, на вход принимает массив"""
        self._array = array

    def array(self) -> list:
        """Метод возвращающий копию списка всех данных"""
        return self._array.copy()

    def array_valid(self) -> list:
        rez = []
        for i in tqdm(range(len(self._array)), desc="Создание валидного списка", ncols=100):
            if self._array[i].check_valid():
                rez.append(self._array[i].info())
        return rez

    def count_invalid_arguments(self):
        """Функция проверки массива на количество некорректных записей в словарях(+ по типу ошибок), возвращаетмассив с их колисеством"""

        rezult = []
        count_inv_err = 0
        count_inv_email = 0
        count_inv_weight = 0
        count_inv_snils = 0
        count_inv_passport_series = 0
        count_inv_university = 0
        count_inv_age = 0
        count_inv_academic_degree = 0
        count_inv_worldview = 0
        count_inv_address = 0
        flag = False
        for i in tqdm(range(len(self._array)),
                      desc="Проверка записей на коректность и получение статистики",
                      ncols=100):
            if not self._array[i].check_email():
                count_inv_email += 1
                flag = True
            if not self._array[i].check_weight():
                count_inv_weight += 1
                flag = True
            if not self._array[i].check_snils():
                count_inv_snils += 1
                flag = True
            if not self._array[i].check_passport_series():
                count_inv_passport_series += 1
                flag = True
            if not self._array[i].check_university():
                count_inv_university += 1
                flag = True
            if not self._array[i].check_age():
                count_inv_age += 1
                flag = True
            if not self._array[i].check_academic_degree():
                count_inv_academic_degree += 1
                flag = True
            if not self._array[i].check_worldview():
                count_inv_worldview += 1
                flag = True
            if not self._array[i].check_address():
                count_inv_address += 1
                flag = True
            if flag:
                count_inv_err += 1
                flag = False


        rezult.append(len(self._array))
        rezult.append(count_inv_err)
        rezult.append(count_inv_email)
        rezult.append(count_inv_weight)
        rezult.append(count_inv_snils)
        rezult.append(count_inv_passport_series)
        rezult.append(count_inv_university)
        rezult.append(count_inv_age)
        rezult.append(count_inv_academic_degree)
        rezult.append(count_inv_worldview)
        rezult.append(count_inv_address)
        return rezult

