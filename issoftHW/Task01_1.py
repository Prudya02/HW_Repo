import os
N = input("Введите строку, состоящую из 0 и 1:\n")
counter = 0
for i in N:
    if i == "0":
        counter += 1
if len(N) - counter < counter:
    counter = len(N)-counter
print(counter)
os.system("pause")