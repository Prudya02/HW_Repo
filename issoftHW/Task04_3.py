import re
name1 = input("введите имя первого файла:")
name2 = input("введите имя второго файла:")


def find_words(name):
    with open(name, 'r') as fin:
        text = fin.read()
    text = text.lower()
    text_arr = re.sub(r'[^\w\s]', '', text)
    text_arr = text_arr.split()
    for word in text_arr:
        is_latin = 1
        for i in word:
            if ord(i) < 97 or ord(i) > 122:
                is_latin = 0
        if is_latin == 0:
            text_arr.remove(word)
    return text_arr


text1 = find_words(name1)
text2 = find_words(name2)
print(set(text1) & set(text2))
