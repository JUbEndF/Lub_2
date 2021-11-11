from Read_file import Read_file
from Valigator import Validator
import re








abs_file_read = "C:/Users/Георгий/Downloads/1.txt" #input("Input path to read file ")

#abs_file_write = input("Input path to write file ")

lines = Read_file(abs_file_read)
lines = lines.text()
lines = re.split(r'\},\{', lines)

lines[0] = re.sub(r'\{',"", lines[0])
for line in lines:
    element = Validator(line)
