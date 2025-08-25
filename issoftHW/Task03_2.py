string = input("Введите строку:\n")
i = 0
reversed_str = ""
while i < len(string):
    if not string[i].isalpha() and not string[i].isdigit():
        reversed_str += string[i]
        i += 1
    begin = i
    while i < len(string) and (string[i].isalpha() or string[i].isdigit()):
        i += 1
    if begin != i:
        reversed_str += string[i-1::-1] if begin == 0 else string[i-1:begin-1:-1]
print(reversed_str)
