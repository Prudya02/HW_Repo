choose = int(input("Вы хотите задать верхнюю границу?\n1:да\n2:нет\n"))
if choose == 1:
    n = int(input("Введите, пожалуйста, N:"))
else:
    n = -1


def gen_arr(b = 100):
    if b >= 0:
        for a in range(1, b+1):
            yield a
    else:
        a = 1
        while True:
            a += 1
            yield a


gen = gen_arr(n)
for item in gen:
    print(item, "-", f"{'не'*(item%2==1)}четное число")
