import numpy as np
def f(x):
    return (np.sqrt(np.exp(x)-1))
I_true = 2.64577597114955 #точное значение.
eps = 0.00001
b = 2
a = 0.1
maxf2 = 7.249 #макс.значение 2-ой произв. на отрезке
maxf4 = 2921.5312 #макс.значение 4-ой произв. на отрезке

h_sred = np.sqrt(24*eps/((b-a)*maxf2)) #необходимый шаг для метода средних прям.
h_simp = np.sqrt(np.sqrt(180*eps/((b-a)*maxf4))) #необходимый шаг для метода симпсона
N1 = int(np.ceil((b-a)/h_sred))
N2 = int(np.ceil((b-a)/h_simp))
h_new1 = (b-a)/N1
h_new2 = (b-a)/N2
print("МЕТОД СРЕДНИХ ПРЯМОУГОЛЬНИКОВ:")
print("Необходимый шаг для достижения заданной точности: ", h_sred)
print("Возьмём количество разбиений N = ", N1)
print("Тогда шаг h = ", h_new1)
S_sred = 0
for i in range(1, N1+1):
    S_sred += f(a+(i-1/2)*h_new1)
S_sred = S_sred*h_new1
print('I_sred при h = ',h_new1,' равен: ', S_sred)
if (I_true-S_sred <= eps):
    print('Невязка r_sred =: ', I_true-S_sred, "что меньше заданной точности ", eps)
print("\nМЕТОД СИМПСОНА:")
print("Необходимый шаг для достижения заданной точности: ", h_simp)
print("Возьмём количество разбиений N = ", N1)
print("Тогда шаг h = ", h_new2)
S_simp = 0
for i in range(N2):
    S_simp = S_simp + f(a+i*h_new2)+4*f(((a+i*h_new2)+a+(i+1)*h_new2)/2)+f(a+(i+1)*h_new2)
S_simp = S_simp*h_new2/6
print('I_simp при h = ',h_new2,' равен: ', S_simp)
if (I_true-S_simp <= eps):
    print('Погрешность r_simp =: ', I_true-S_simp, "что меньше заданной точности ", eps)
