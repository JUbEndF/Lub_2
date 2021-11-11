import re

class Read_file:
    '''Класс чтения принимает путь к файлу и редактирует полученый из него текст'''
    _file_path: str
    _text: str

    def __init__(self, path: str) -> None:
        self._file_path = path
        read = open(path, "r")
        self._text = read.read()
        read.close()
        self._text = re.sub('\n', '', self._text)
        self._text = re.sub('\ +', ' ', self._text)
        self._text = re.sub(r'\[', '', self._text)
        self._text = re.sub(r'\]', '', self._text)
        self._text = re.sub(r'"', '', self._text)
        self._text = re.split(r'\},\{', self._text)

        self._text[0] = re.sub(r'\{', "", self._text[0])
        for i in range(len(self._text)):
            self._text[i] = re.split(r',', self._text[i])
            for j in range(len(self._text[i])):
                self._text[i][j] = re.findall(r':(.+)', self._text[i][j])


    def text(self) -> str:
        return str(self._text)