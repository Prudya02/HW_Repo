choose = int(input("Вы хотите задать верхнюю границу?\n1:да\n2:нет\n"))
if choose == 1:
    n = int(input("Введите, пожалуйста, N:"))
else:
    n = -1


def gen_arr(b):
    def prime(c):
        if c == 1 or c == 4:
            return 0
        for i in range(2, int(c/2)):
            if c % i == 0:
                return 0
        return 1
    if b >= 0:
        for a in range(1, b+1):
            if prime(a):
                yield a
    else:
        a = 1
        while True:
            a += 1
            if prime(a):
                yield a


gen = gen_arr(n)
for item in gen:
    print(item)
