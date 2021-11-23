from Read_file import Read_file
from ValigatorCollection import Validator_list



abs_file_read = "C:/Users/Георгий/Downloads/1.txt" #input("Input path to read file ")

#abs_file_write = input("Input path to write file ")

lines = Read_file(abs_file_read)

data = Validator_list(lines.array_list())

rez = data.count_invalid_arguments()

print(rez)
