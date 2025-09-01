#Вариант 7
import numpy as np
import pprint
rclos = [bin(0x45C862)[2:],bin(0x1A0891C3)[2:],bin(0x4E1F8D11)[2:]]
rclosh = [bin(0x400032)[2:], bin(0x1000008C)[2:], bin(0x4000002A)[2:]]
print("Хар.многочлен:", rclosh)
print("Нач.значение :", rclos)
new = [[0 for i in range(23)], [0 for i in range(29)], [0 for i in range(31)]]


def LSFR():
    for i in range(3):
        for j in range (len(rclos[i])):
            new[i][j] = int(rclos[i][j]) >> int(rclosh[i][j])
    return new


new = LSFR()
for i in range (3):
    print(new[i])