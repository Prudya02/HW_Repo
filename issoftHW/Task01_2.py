import os
letter = input("Введите букву: ")
string = input("Введите строку, в которой будете искать:\n")
is_got = 0
for i in string:
    if i == letter:
       is_got = 1
if is_got == 0:
    print("Буква", letter, "не встречается в строке", string)
else:
    print("Буква", letter, "встречается в строке", string)
os.system("pause")