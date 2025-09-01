#VARIANT 7, a1 = 0.01; a2 = 0.05
import math

import numpy as np
import matplotlib.pyplot as plt
sample_2 = [13.3, 13.4, 12.4, 13.2, 12.0, 12.3, 12.1, 11.8,12.7,12.6,12.0,13.1,11.8,11.5,12.9,11.3,11.5,12.2,11.2,10.6,11.6,11.1,
            10.7,12.4,11.1,12.3,11.2,12.5,11.8,12.0,13.1,11.7,12.0,11.9,12.9,11.7,11.6]
sample_3 = [11.8,13.2,11.7,12.3,11.5,11.5,11.3,11.5,11.7,11.8,11.6,12.2,11.4,11.6,11.9,11.1,11.2,11.1,10.5,10.5,11.0,11.3,
            11.0,12.4,11.5,10.4,11.0,11.3,11.1,11.6,11.5,11.6,11.0,11.0,11.6,10.6,11.6]
n = len(sample_2)
sum_vz = 0
sum_2 = 0
sredkvy = 0
sredkvx = 0
for i in range(n):
    sredkvx += (sample_2[i] - sum(sample_2)/n)**2
    sredkvy += (sample_3[i] - sum(sample_3)/n)**2
    sum_2 += sample_2[i]*sample_2[i]
    sum_vz += sample_2[i]*sample_3[i]
sredkvy = sredkvy/n
sredkvx = sredkvx/n
#Расчёт коэффициентов линейной регрессии
a = (n*sum_vz-sum(sample_2)*sum(sample_3))/((n*sum_2)-sum(sample_2)*sum(sample_2))
b = sum(sample_3)/n - sum(sample_2)/n * a
print('a =', a)
print('b=',b)
#Строим корелляционное поле
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10,8))
ax.set_title('Рисунок 1. Корелляционное поле для значений второго и третьего ВР.')
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Второй ряд", fontsize=16)
ax.set_ylabel("Третий ряд, С", fontsize=16)
for i in range(len(sample_2)):
    plt.scatter(sample_2[i], sample_3[i], color='orange')
y = lambda x: a*x+b
x = np.linspace(8, 15, 100)
plt.plot(x, y(x))
plt.show()
#Вычисляем дисперсию отклонения
r = 0.6662009037066482 #взяли из предыдущей работы
delta = sredkvy*(1-r*r)
print("Дисперсия отклонения:", delta)
#Вычисляем стандартные случайные погрешности
delta_a = math.sqrt(delta)/(math.sqrt(sredkvx)*math.sqrt(n-2))
delta_b = math.sqrt(delta)/(math.sqrt(n-2))*math.sqrt(1+sum(sample_2)*sum(sample_2)/(n*n*sredkvx))
print("Стандартные случайные погрешности:\ndelta_a:", delta_a, "\ndelta_b:", delta_b)
#Оценить значимость коэффициентов регрессии. Для этого выдвинуть нулевую гипотезу
Ta = a/delta_a
Tb = b/delta_b
print("Критерии Стьюдента: \nTa:", Ta, "\nTb:", Tb)
k = n-2
tkr1 = 2.720 #0.01
tkr2 = 2.030 #0.05

if Ta < tkr1:
    print("Для a = 0.01 нет оснований отергать 0-ую гипотезу")
else:
    print("Для a = 0.01 нулевая гипотеза опровергнута. Величина а - значима")
if Tb < tkr1:
    print("Для a = 0.01 нет оснований отергать 0-ую гипотезу")
else:
    print("Для a = 0.01 нулевая гипотеза опровергнута. Величина b - значима")


if Ta < tkr2:
    print("Для a = 0.05 нет оснований отергать 0-ую гипотезу")
else:
    print("Для a = 0.05 нулевая гипотеза опровергнута. Величина а - значима")
if Tb < tkr2:
    print("Для a = 0.05 нет оснований отергать 0-ую гипотезу")
else:
    print("Для a = 0.05 нулевая гипотеза опровергнута. Величина b - значима")
