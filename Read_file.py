import json
from Data_info import Data


class Read_file:
    '''Класс чтения принимает путь к файлу и получает из него текст'''
    _file_path: str
    _array: list = []

    def __init__(self, file_path: str) -> None:
        """Конструктор класса, на вход принимает путь к файлу"""
        self._file_path = file_path
        data = json.load(open(self._file_path, encoding="windows-1251"))
        for i in data:
            self._array.append(Data(i.copy()))

    def array_list(self) -> list:
        return self._array.copy()


