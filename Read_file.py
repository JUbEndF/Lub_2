import re

class Read_file:
    _file_path: str
    _text: str

    def __init__(self, path: str) -> None:
        self._file_path = path
        read = open(path, "r")
        self._text = read.read()
        read.close()
        self._text = re.sub('\n', '', self._text)
        self._text = re.sub('\ +', '', self._text)
        self._text = re.sub(r'\[', '', self._text)
        self._text = re.sub(r'\]', '', self._text)
        self._text = re.sub(r'"', '', self._text)

    def text(self) -> str:
        return str(self._text)