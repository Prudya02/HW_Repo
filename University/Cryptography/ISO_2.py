# ВАРИАНТ 7, Владислав Прудникович
import math

N = 7
q = 9
r = 11
k = 4096 - 11 * q * r
round_key1 = [1, 2, 3, 4, 5, 6, 7, 8]
round_key2 = [6, 7, 8, 9, 10, 11, 12, 1]
round_key3 = [11, 12, 1, 2, 3, 4, 5, 6]
S1 = [3, 7, 14, 9, 8, 10, 15, 0, 5, 2, 6, 12, 11, 4, 13, 1]
S2 = [11, 5, 1, 9, 8, 13, 15, 0, 14, 4, 2, 3, 12, 7, 10, 6]
print("Блок S1:", S1)
print("Блок S2:", S2)
round_key1_bin = [[0 for i in range(8)] for j in range(3)]
k_bin = str(bin(k))[2:]
k_arr = [*map(int, str(k_bin))]
print("k bin = ", k_arr)
for i in range(8):
    if k_arr[round_key1[i] - 1] == 1:
        round_key1_bin[0][i] = 1
    if k_arr[round_key2[i] - 1] == 1:
        round_key1_bin[1][i] = 1
    if k_arr[round_key3[i] - 1] == 1:
        round_key1_bin[2][i] = 1
    else:
        round_key1_bin[2][i] = 0
print("ключ для первой итерации:", round_key1_bin[0])
print("ключ для второй итерации:", round_key1_bin[1])
print("ключ для третьей итерации:", round_key1_bin[2], '\n')
result = str(bin(N * 7))[2:]


def do_iteration(result):
    x_bin = result
    while len(x_bin) < 8:
        x_bin = '0' + x_bin
    x_arr = [*map(int, str(x_bin))]
    print("x bin = ", x_arr)
    sum = [0] * 8
    for i in range(8):
        sum[i] = round_key1_bin[counter][i] ^ x_arr[i]
    print("Результат сложения:", sum)
    sum_div = [0] * 2
    for i in range(4):
        sum_div[0] += sum[i] * math.pow(2, 3 - i)
        sum_div[1] += sum[i + 4] * math.pow(2, 3 - i)
    print("Разделенная сумма:", sum_div)
    sum_div[0] = S1[int(sum_div[0])]
    sum_div[1] = S2[int(sum_div[1])]
    print("результат применения блоков:", sum_div)
    sum_div[0] = str(bin(sum_div[0])[2:])
    while len(sum_div[0]) < 4:
        sum_div[0] = '0' + sum_div[0]
    sum_div[1] = str(bin(sum_div[1])[2:])
    while len(sum_div[1]) < 4:
        sum_div[1] = '0' + sum_div[1]
    print("Результат в бинарном виде:", sum_div)
    sum_new = sum_div[0] + sum_div[1]
    result = sum_new[3:] + sum_new[:3]
    print("Результат ", counter + 1, " итерации:", result, '\n')
    return result


for counter in range(3):
    result = do_iteration(result)
print("Заменим последний бит исходного сообщения\n")
result2 = str(bin(N * 7 - 1))[2:]
for counter in range(3):
    result2 = do_iteration(result2)
print("Сравним результаты:", result, "и", result2, "или в десятичной системе:", int(result, 2), "и", int(result2, 2))
