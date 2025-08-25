n1 = int(input("Введите первое число:"))
n2 = int(input("ведите второе число:"))
NOD = 0
n3 = n1
n4 = n2
if n1 <= 1 or n2 <= 1:
    print("Числа не могут быть взаимно простыми")
else:
    is_prime = 1
    while is_prime == 1:
        if n2 >= n1:
            if n2 % n1 == 0:
                NOD = n1
                is_prime = 0
            else:
                n2 = n2-n1
        else:
            if n1 % n2 == 0:
                NOD = n2
                is_prime = 0
            else:
                n1 = n1-n2
    if NOD > 1:
        print(n3,"и",n4, "не взаимно простые")
    else:
        print(n3,"и",n4, "взаимно простые")
