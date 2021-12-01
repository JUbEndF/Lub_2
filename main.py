from Read_file import Read_file
from ValigatorCollection import Validator_list
from Write_file import Write_file
from sort import sort_puzirek
import argparse
import pickle

parser = argparse.ArgumentParser("Input & output path")
parser.add_argument("-read", type=str, default="1.txt", help="Read path")
parser.add_argument("-write", type=str, default="rez.txt", help="Write path")


pars = parser.parse_args()

lines = Read_file(pars.read)

data = Validator_list(lines.array_list())

rez = data.count_invalid_arguments()

write = Write_file(pars.write)
write.write_file(data.array())

print("Валидных записей:", rez[0])
print("Невалидных записей:", rez[1])
print("Ошибка в написании электронной почты: ", rez[2])
print("Ошибка в написании веса: ", rez[3])
print("Ошибка в написании СНИЛСа: ", rez[4])
print("Ошибка в написании серии паспорта: ", rez[5])
print("Ошибка в написании университета: ", rez[6])
print("Ошибка в написании возраста: ", rez[7])
print("Ошибка в написании академической степени: ", rez[8])
print("Ошибка в написании вероисповедания: ", rez[9])
print("Ошибка в написании адреса: ", rez[10])

arr = data.array_valid()
arr = sort_puzirek(arr)

with open('data.pickle', 'wb') as f:
    pickle.dump(arr, f)

with open('data.pickle', 'rb') as f:
    data_new = pickle.load(f)
for i in data_new:
    print(i)

