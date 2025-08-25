is_bad = 1
while is_bad:
    s_first = int(input("Введите начальную систему счисления : "))
    if s_first < 2 or s_first > 36:
        print("Система счисления не соответствует ограничениям [2,36]")
    else:
        is_bad = 0
is_bad = 1
is_neg = 0
while is_bad:
    a = (input(f"Введите число из заданной ({s_first}) системы счисления:"))
    #is_neg = int(a) < 0
    #if is_neg:
        #a = -int(a)
    s_buf = s_first
    if int(s_buf) >= 10:
        s_buf = chr(55+int(s_buf))
    else:
        s_buf = chr(48+s_buf)
    if ord(a) >= ord(s_buf):
        print(f"Введенное число не принадлежит заданной ({s_first}) системе счисления")
    else:
        is_bad = 0
is_bad = 0
while is_bad:
    s_second = int(input("Введите предпочитаемую систему счисления : "))
    if s_second < 2 or s_second > 36:
        print("Система счисления не соответствует ограничениям [2,36]")
    else:
        is_bad = 0
is_bad = 1
is_neg = 0