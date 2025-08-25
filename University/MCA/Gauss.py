import numpy as np
import scipy
from scipy import special
I_true = 2.64577597114955 #точное значение.
a = 0.1
b = 2
n = 5
def f(x):
    return 0.95*(np.sqrt(np.exp(0.95*x+1.05)-1))
Ai = [0.236927, 0.478629, 0.236927, 0.478629, 0.568889]
Xi = scipy.special.legendre(5).roots
print("Корни многочлена Лежандра", Xi)
S_gauss = 0
for i in range (5):
    S_gauss+= Ai[i]*f(Xi[i])
print("Значение по формуле НАСТ Гаусса при n = 4: ", S_gauss)
print("Точное значение интеграла: ", I_true)
print("Погрешность : ", I_true-S_gauss)
S_gauss_arr = [0,0,0,0,0]
for i in range (5):
    S_gauss_arr[0]+=Ai[i]
    S_gauss_arr[1]+= Ai[i]*Xi[i]
    S_gauss_arr[2]+= Ai[i] * Xi[i]**2
    S_gauss_arr[3]+= Ai[i] * Xi[i]**3
    S_gauss_arr[4]+= Ai[i] * Xi[i]**4
print(S_gauss_arr)

