import os
number = int(input("Введите натуральное число:"))
i = 2
summa = 0
number_buf = number
if number == 1:
    print("Простых делителей нет")
else:
    while number/2 >= i:
        is_found = 0
        while number_buf % i == 0 and number_buf > 1:
            is_found = 1
            number_buf = number_buf / i
        if is_found == 1:
            summa += i
        i+=1
if summa !=0:
    print(summa)
else:
    print(number)
os.system("pause")