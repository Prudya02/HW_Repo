#VARIANT 7, a1 = 0.01; a2 = 0.05
import math
import os
import numpy as np
import matplotlib.pyplot as plt
#1.Построение кореляционного поля.

sample_2 = [13.3,13.4,12.4,13.2,12.0,12.3,12.1,11.8,12.7,12.6,12.0,13.1,11.8,11.5,12.9,11.3,11.5,12.2,11.2,10.6,11.6,11.1,
            10.7,12.4,11.1,12.3,11.2,12.5,11.8,12.0,13.1,11.7,12.0,11.9,12.9,11.7,11.6]
sample_3 = [11.8,13.2,11.7,12.3,11.5,11.5,11.3,11.5,11.7,11.8,11.6,12.2,11.4,11.6,11.9,11.1,11.2,11.1,10.5,10.5,11.0,11.3,
            11.0,12.4,11.5,10.4,11.0,11.3,11.1,11.6,11.5,11.6,11.0,11.0,11.6,10.6,11.6]
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10,8))
ax.set_title('Рисунок 1. Корелляционное поле для значений второго и третьего ВР.')
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Второй ряд",fontsize=16)
ax.set_ylabel("Третий ряд, С",fontsize=16)
for i in range(len(sample_2)):
    plt.scatter(sample_2[i], sample_3[i], color='orange')
plt.plot(0,0)
plt.plot(15,15)


#2. Расчёт коэффициента корелляции

sx, sy, sredx, sredy, srkvx, srkvy, srkvxy = [0 for i in range (7)]
for i in range (len(sample_2)):
    sredx += sample_2[i]
    sredy += sample_3[i]
sredx = sredx / (len(sample_2))
sredy = sredy / (len(sample_3))
for i in range (len(sample_2)):
    srkvx += (sample_2[i] - sredx) * (sample_2[i] - sredx)
    srkvy += (sample_3[i] - sredy) * (sample_3[i] - sredy)
    srkvxy += (sample_2[i] - sredx)*(sample_3[i]-sredy)
srkvxy = srkvxy/len(sample_2)
srkvx = math.sqrt(srkvx / (len(sample_2)))
srkvy = math.sqrt(srkvy / (len(sample_3)))
r = srkvxy/(srkvx*srkvy)
print("Коэффициент корреляции второго и третьего рядов  равен:", r)
#3
delta_r = np.sqrt((1-r*r)/(len(sample_2)-2))
print("Cреднеквадратическая ошибка линейного коэффициента корреляции:", delta_r)
t = r/delta_r
print("Критерий Стьюдента:", t)
print("Количество степеней свободы k = ", len(sample_2)-2)
tkr1 = 2.720
tkr2 = 2.030
print("Критическое значение для a = 0.01:", tkr1)
print("Критическое значение для a = 0.05:", tkr2)
if t < tkr1 :
    print("Для a = 0.01 нет оснований отергать 0-ую гипотезу")
else:
    print("Для a = 0.01 нулевая гипотеза опровергнута. R - значима")
if t < tkr2 :
    print("Для a = 0.05 нет оснований отергать 0-ую гипотезу")
else:
    print("Для a = 0.05 нулевая гипотеза опровергнута. R - значима")
gamma1 = 0.99 #0.495*2
gamma2 = 0.95 #0.475*2
print("Надежность для a1=0.01:", gamma1)
print("Надежность для a2=0.05:", gamma2)
z1 = 2.578
z2 = 1.96
a1 = 0.5*np.log((1+r)/(1-r))-z1/np.sqrt(len(sample_2)-3)
a2 = 0.5*np.log((1+r)/(1-r))-z2/np.sqrt(len(sample_2)-3)
b1 = 0.5*np.log((1+r)/(1-r))+z1/np.sqrt(len(sample_2)-3)
b2 = 0.5*np.log((1+r)/(1-r))+z2/np.sqrt(len(sample_2)-3)
tet_low1 = (np.exp(2*a1)-1)/(np.exp(2*a1)+1)
tet_low2 = (np.exp(2*a2)-1)/(np.exp(2*a2)+1)
tet_high1 = (np.exp(2*b1)-1)/(np.exp(2*b1)+1)
tet_high2 = (np.exp(2*b2)-1)/(np.exp(2*b2)+1)
print("\nДля a = 0.01:\n Z = ",z1,"\n Доверительный интервал: [",tet_low1,";",tet_high1,"]")
print("\nДля a = 0.01:\n Z = ",z2,"\n Доверительный интервал: [",tet_low2,";",tet_high2,"]")
plt.show()
