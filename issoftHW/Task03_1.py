def convert(s1, s2, a):
    dot = a.find('.')
    int_dec_value = 0
    float_dec_value = 0
    if dot == -1:
        for i in range(len(a)):
            value = ord(a[i]) - 48 if ord(a[i]) < 58 else ord(a[i]) - 55
            int_dec_value += value*(s1**(len(a)-i-1))
    else:
        for i in range(len(a[:dot])):
            value = ord(a[i]) - 48 if ord(a[i]) < 58 else ord(a[i]) - 55
            int_dec_value += value * (s1 ** (len(a[:dot]) - i - 1))
        for i in range(1, len(a[dot:])):
            value = ord(a[i+len(a[:dot])]) - 48 if ord(a[i+len(a[:dot])]) < 58 else ord(a[i+len(a[:dot])]) - 55
            float_dec_value += value*1/(s1**i)
    new_number = ''
    while int_dec_value > s2:
        new_number += str(int_dec_value % s2) if int_dec_value % s2 < 10 else chr(55+int_dec_value % s2)
        int_dec_value = int_dec_value // s2
    new_number += str(int_dec_value % s2) if int_dec_value % s2 < 10 else chr(55+int_dec_value % s2)
    new_number = new_number[::-1]
    if float_dec_value == 0:
        return new_number
    else:
        new_number+='.'
        for i in range(16):
            new_number += str(int(float_dec_value*s2)) if int(float_dec_value*s2) < 10 else chr(55+int(float_dec_value*s2))
            float_dec_value = float_dec_value*s2-int(float_dec_value*s2)
        return new_number


is_bad = 1
while is_bad:
    s_first = int(input("Введите начальную систему счисления : "))
    if s_first < 2 or s_first > 36:
        print("Система счисления не соответствует ограничениям [2,36]")
    else:
        is_bad = 0
is_bad = 1
while is_bad:
    s_second = int(input("Введите предпочитаемую систему счисления : "))
    if s_second < 2 or s_second > 36:
        print("Система счисления не соответствует ограничениям [2,36]")
    else:
        is_bad = 0
max_system_value = 47 + s_first if s_first <= 10 else 54 + s_first
is_bad = 1
is_neg = 0
while is_bad:
    is_bad = 0
    numb = (input(f"Введите число из заданной ({s_first}) системы счисления:"))
    is_neg = numb[0] == '-'
    if is_neg:
        numb = numb[1:]
    for i in numb:
        if ord(i) > max_system_value:
            print(f"Введенное число не принадлежит заданной ({s_first}) системе счисления")
            is_bad = 1
            break
new_numb = convert(s_first, s_second, numb)
if is_neg:
    numb = '-'+numb
    new_numb = '-'+new_numb
print(f"{numb}({s_first})->{s_second}={new_numb}({s_second})")
