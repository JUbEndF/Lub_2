from Read_file import Read_file
from ValigatorCollection import Validator_list
from Write_file import Write_file



abs_file_read = "C:/Users/Георгий/Downloads/1.txt" #input("Input path to read file ")

abs_file_write = 'C:/Users/Георгий/PycharmProjects/Lub_2/rez.txt'#input("Input path to write file ")

lines = Read_file(abs_file_read)

data = Validator_list(lines.array_list())

rez = data.count_invalid_arguments()

write = Write_file(abs_file_write)
write.write_file(data.array())

print("Валидных записей:", rez[0])
print("Невалидных записей:", rez[1])
print("Ошибка в написании номера телефона: ", rez[2])
print("Ошибка в написании веса: ", rez[3])
print("Ошибка в написании СНИЛСа: ", rez[4])
print("Ошибка в написании номера паспорта: ", rez[5])
print("Ошибка в написании профессии: ", rez[6])
print("Ошибка в написании возраста: ", rez[7])
print("Ошибка в написании академического разряда: ", rez[8])
print("Ошибка в написании вероисповедания: ", rez[9])
print("Ошибка в написании адреса: ", rez[10])
