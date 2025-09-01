import math
p = 5/6
p_otk = 1
n = 1
p0 = 0
while p_otk > 0.1:
    p0 = 0
    for i in range(n+1):
        p0 += p**i/math.factorial(i)
    p0 = 1/p0
    p_otk = p**n/math.factorial(n) * p0
    print("Вероятность отказа для n =", n, "равна:", p_otk)
    if p_otk > 0.1:
        n += 1
print("Необходимое число телефонов:", n)
