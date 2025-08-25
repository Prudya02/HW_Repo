import os
numb = input("Введите дробное число:\n")
summa = 0
for i in numb:
    if i != '.':
        summa += int(i)
print(summa)
os.system("pause")