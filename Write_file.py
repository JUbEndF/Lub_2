import json
from tqdm import tqdm

class Write_file:
    _file_path: str

    def __init__(self, file_path) -> None:
        '''Класс принимает путь к файлу для записи данных'''
        self._file_path = file_path

    def write_file(self, array: list) -> None:
        """Функция записи в файл, принимает на вход сам массив для записи"""

        tmp = []
        for i in tqdm(range(len(array)), desc="Запись результата валидации в файл", ncols=100):
            if array[i].check_valid():
                tmp.append(array[i].info())
        json.dump(tmp, open(self._file_path, "w", encoding="windows-1251"), ensure_ascii=False, sort_keys=False, indent=4)