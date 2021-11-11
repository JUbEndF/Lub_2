from Read_file import Read_file
#from Valigator import Validator
import re



abs_file_read = "C:/Users/Георгий/Downloads/1.txt" #input("Input path to read file ")

#abs_file_write = input("Input path to write file ")

lines = Read_file(abs_file_read)
lines = lines.text()

print(lines)


