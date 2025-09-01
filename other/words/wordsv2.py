"""Код ниже находит слова в русском языке, буквы которых отличаются друг от друга сдвигом на n
В качестве исходных данных используется словарь для т9, поэтому программа часто выдаёт основы слов,
среди которых можно выделить полноценные слова
Также, в данном словаре отсутствуют аббревиатуры, (будут отсутстовать пары вида: квас -> лгбт)"""
import requests
from collections import defaultdict
response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')
text = response.content.decode('cp1251')
text2 = text[55:]
massive = text2.split('\n')
massive2 = []
#response = 'russian.txt'
for word in massive:
    if "-" not in word and "." not in word and "'" not in word and " " not in word:
        massive2.append(word.lower())
grouped_guys = defaultdict(list)

for word in massive2:
    leng = len(word)
    if leng < 35:
        grouped_guys[leng].append(word)
alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#print(grouped_guys)
def word_to_tuple(word):
    return tuple(alph.index(let) + 1 for let in word)


def find_same(words_list):
    num_set = set()
    word_to_num = {}

    for word in words_list:
        num_repr = word_to_tuple(word)
        num_set.add(num_repr)
        word_to_num[num_repr] = word

    found_pairs = []

    for num_word in num_set:
        current_max = max(num_word)

        for shift in range(1, 33 - current_max):
            shifted_word = tuple(x + shift for x in num_word)

            if shifted_word in num_set:
                word1 = word_to_num[num_word]
                word2 = word_to_num[shifted_word]
                found_pairs.append((word1, word2, shift))

    return found_pairs

target_length = 6 ### Выбираем длину здесь
#target_length = input("Введите длину проверяемых слов для сдвига")
mas = grouped_guys[target_length]
#print(mas[:100])
####Подумать над ускорением для большей длины
print(f"Анализируем {len(mas)} слов длиной {target_length}")
found_pairs = find_same(mas)

for word1, word2, shift in found_pairs:
    print(f"{word1} -> {word2} (сдвиг: +{shift})")