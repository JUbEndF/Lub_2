import re

class Read_file:
    '''Класс чтения принимает путь к файлу и получает из него текст'''
    _file_path: str
    _text: str

    def __init__(self, path: str) -> None:
        self._file_path = path
        read = open(path, "r")
        self._text = read.read()
        read.close()

    def text(self) -> str:
        return str(self._text)