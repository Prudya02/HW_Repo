import re
name = input("введите название вашего файла:")
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
diction = {}
for word in text_arr:
    diction[word] = diction.get(word, 0) + 1
sort_arr = []
for key, value in diction.items():
    sort_arr.append((value, key))
    sort_arr.sort(reverse=True)
max_freq = sort_arr[0][0]
for i in range(len(sort_arr)):
    if sort_arr[i][0] == max_freq:
        print(sort_arr[i][1])
#print(sort_arr)

