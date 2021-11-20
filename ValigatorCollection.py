import re
from Data_info import Data

class Validator_list:
    data: list

    def __init__(self, text: str) -> None:
        _text = re.sub('\n', '', text)
        _text = re.sub('\ +', ' ', _text)
        _text = re.sub(r'\[', '', _text)
        _text = re.sub(r'\]', '', _text)
        _text = re.sub(r'"', '', _text)
        _text = re.split(r'\},\s+{', _text)

        _text[0] = re.sub(r'\{', "", _text[0])
        for i in range(len(_text)):
            _text[i] = re.split(r',', _text[i])
            for j in range(len(_text[i])):
                _text[i][j] = re.findall(r':(.+)', _text[i][j])
        for i in range(len(_text)):
            self.data.append(Data(_text[i]))


    def data(self) -> list:
        return self._data

    #def data(self, index: int) -> dict:



