import math
import re
import numpy as np


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

alphabet =['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П',
           'Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
interpr =[]
for i in range(len(alphabet)):
    interpr.append(i)
print("Алфавит:", alphabet)
print("Интерпритация:",interpr)
print("Введите текст:")
is_good = 0
word = 0
while is_good == 0:
    is_good = 1
    word = input()
    for i in range (len(word)):
        if word[i] not in alphabet:
            print("Символа", word[i], "нет в исходном алфавите")
            is_good = 0
print("Слово веедено успешно")
print("Выберите способ шифрования\n 1. Шифр Хилла\n2. Афинный шифр")
type = 0
is_good = 0
while (is_good == 0):
    type = input()
    if int(type) == 1 or int(type) == 2:
        is_good = 1
if int(type) == 1:
    print("Введите ключ:")
    is_good = 0
    determ = 0
    key = 0
    while is_good == 0:
        is_good = 1
        key = input()
        key = key.split()
        if len(key) != 4:
            print("Длина ключа должна равняться 4 ")
            is_good = 0
        if is_good == 1:
            for i in range(len(key)):
                if int(key[i]) >= len(alphabet):
                    print("Элемент", key[i], "не лежит в кольце Z_33")
                    is_good = 0
        if is_good == 1:
            determ = int(key[0]) * int(key[3]) - int(key[1]) * int(key[2])
            if math.gcd(determ, len(alphabet)) != 1:
                # print(math.gcd(determ,33))
                print("Определитель матрицы ключа должен быть взаимно простым с ", len(alphabet))
                is_good = 0
    print("Ключ удовлетворяет всем условиям")
    print("Введите 1 для зашифровки или введите 2 для дешифровки сообщения:")
    to_do = 0
    is_good = 0
    while (is_good == 0):
        to_do = input()
        if int(to_do) == 1 or int(to_do) == 2:
            is_good = 1
    if int(to_do) == 1:
        print("Начнём процесс шифрования")
        print("Разобьём слово на блоки:")
        if np.mod(len(word), 2) == 1:
            word = word + "А"
        divided = re.findall('.{%s}' % 2, word)
        shifr = []
        print(divided)
        for i in range(len(divided)):
            number1 = alphabet.index(divided[i][0]) * int(key[0]) + alphabet.index(divided[i][1]) * int(key[2])
            modnumber1 = np.mod(number1, 33)
            number2 = alphabet.index(divided[i][0]) * int(key[1]) + alphabet.index(divided[i][1]) * int(key[3])
            modnumber2 = np.mod(number2, 33)
            shifr.append(alphabet[modnumber1])
            shifr.append(alphabet[modnumber2])
        print("Зашифрованный текст:", shifr)
    if int(to_do) == 2:
        print("Начнём процесс дешифровки")
        determ_inverse = mulinv(determ, len(alphabet))
        print("Обратный в кольце вычетов детерминант:", determ_inverse)
        key_inverse = [np.mod(int(key[3]) * determ_inverse, 33), np.mod(-int(key[1]) * determ_inverse, 33),
                       np.mod(-int(key[2]) * determ_inverse, 33), np.mod(int(key[0]) * determ_inverse, 33)]
        print("Обратная матрица ключа:", key_inverse)
        print("Разобьём слово на блоки:")
        if np.mod(len(word), 2) == 1:
            word = word + "А"
        divided = re.findall('.{%s}' % 2, word)
        deshifr = []
        print(divided)
        for i in range(len(divided)):
            number1 = alphabet.index(divided[i][0]) * int(key_inverse[0]) + alphabet.index(divided[i][1]) * int(
                key_inverse[2])
            modnumber1 = np.mod(number1, 33)
            number2 = alphabet.index(divided[i][0]) * int(key_inverse[1]) + alphabet.index(divided[i][1]) * int(
                key_inverse[3])
            modnumber2 = np.mod(number2, 33)
            deshifr.append(alphabet[modnumber1])
            deshifr.append(alphabet[modnumber2])
        print("Расшифрованный текст:", deshifr)
if int(type) == 2:
    print("Введите a:")
    is_good = 0
    a = 0
    b = 0
    while (is_good == 0):
        is_good = 1
        a = input()
        if math.gcd(int(a), len(alphabet)) != 1:
            print("Число а должно быть взаимно простым с", len(alphabet))
            is_good = 0
    print("Введите b:")
    b = input()
    print("Введите 1 для зашифровки или введите 2 для дешифровки сообщения:")
    to_do = 0
    is_good = 0
    while (is_good == 0):
        to_do = input()
        if int(to_do) == 1 or int(to_do) == 2:
            is_good = 1
    if int(to_do) == 1:
        shifr = []
        for i in range(len(word)):
            shifr.append(alphabet[np.mod(int(a) * alphabet.index(word[i]) + int(b), len(alphabet))])
        print(shifr)
    if int(to_do) == 2:
        deshifr = []
        a_inv = mulinv(int(a), len(alphabet))
        print("Обратное число для а:", a_inv)
        for i in range(len(word)):
            deshifr.append(alphabet[np.mod(int(a_inv) * (alphabet.index(word[i]) - int(b)), len(alphabet))])
        print(deshifr)
