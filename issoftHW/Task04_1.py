morze = {'a': '.-',     'b': '-...',   'c': '-.-.', 'd': '-..',    'e': '.',      'f': '..-.',
         'g': '--.',    'h': '....',   'i': '..', 'j': '.---',   'k': '-.-',    'l': '.-..',
         'm': '--',     'n': '-.',     'o': '---', 'p': '.--.',   'q': '--.-',   'r': '.-.',
         's': '...',    't': '-',      'u': '..-', 'v': '...-',   'w': '.--',    'x': '-..-',
         'y': '-.--',   'z': '--..',   '0': '-----', '1': '.----',  '2': '..---', '3': '...--',
         '4': '....-',  '5': '.....', '6': '-....',  '7': '--...',  '8': '---..', '9': '----.'}
name = input("введите название вашего файла:")
with open(name, 'r') as fin:
    text = fin.read()
text = text.lower()
code = 1
i = 0
while text[i] == ' ':
    i += 1
if not text[i].isalpha() and not text[i].isdigit():
    code = 0
print(f"{'Декодирование'*(not code) + 'Кодирование'*code } исходного файла:")
new_text = ''
if code == 1:
    k = i
    while k < len(text):
        if text[k] == '\n':
            new_text += '   \n'
            k+=1
        elif text[k] == ' ':
            new_text += '  '
            while text[k] == ' ':
                k += 1
        else:
            new_text += morze.get(text[k])+' '
            k += 1
    with open('cod.' + name, 'w') as fo:
        fo.write(new_text)
    print(new_text)
else:
    k = i
    while k < (len(text)):
        if text[k] == '\n':
            new_text += '\n'
            k += 1
        elif k < len(text) - 1 and text[k] == ' ' and text[k+1] == ' ':
            new_text += ' '
            k += 2
        elif text[k] == ' ':
            k += 1
        else:
            letter = ''
            while k < len(text) and text[k] != ' ':
                letter += text[k]
                k += 1
            new_text += (list(morze.keys())[list(morze.values()).index(letter)])
    i = 0
    while new_text[i] == ' ':
        i += 1
    if new_text[i].isalpha():
        new_text = ' '*i + new_text[i:].capitalize()
    with open(name[4:], 'w') as fo:
        fo.write(new_text)
    print(new_text)
