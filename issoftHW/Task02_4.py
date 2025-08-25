choose = int(input("Вы хотите задать верхнюю границу?\n1:да\n2:нет\n"))
if choose == 1:
    n = int(input("Введите, пожалуйста, N:"))
else:
    n = -1


def gen_arr(b):
    def palindrome(c):
        if c < 10:
            return 1
        c_buf = c
        subs = 1
        while c_buf >= 10:
            c_buf = c_buf // 10
            subs = subs*10
        if c % 10 == c_buf:
            new = (c-subs*c_buf)//10
            if new == 0:
                return 1
            if new * 100 >= subs:
                return palindrome(new)
            new_buf = new
            counter = 1
            while new_buf < subs:
                new_buf = new_buf*10
                counter = counter*10
            if counter > 100:
                if new % (counter//100) == 0:
                    return palindrome(new // (counter//100))
        return 0
    if b >= 0:
        for a in range(1, b+1):
            if palindrome(a) and a >= 10:
                yield a
    else:
        a = 1
        while True:
            a += 1
            if palindrome(a) and a >= 10:
                yield a


gen = gen_arr(n)
for item in gen:
    print(item)
