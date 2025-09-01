import math
import numpy as np
import matplotlib.pyplot as plt
Sample_x = [16, 18, 21, 24, 26, 31, 34, 37, 41, 45, 47, 48]
Sample_Y = [234, 249, 247, 287, 260, 262, 307, 280,357,410, 389,317]
####Уравнение линейной регрессии
n = len(Sample_x)
sum_vz = 0
sum_2 = 0
sredkvy = 0
sredkvx = 0
for i in range(n):
    sredkvx += (Sample_x[i] - sum(Sample_x) / n) ** 2
    sredkvy += (Sample_Y[i] - sum(Sample_Y) / n) ** 2
    sum_2 += Sample_x[i] * Sample_x[i]
    sum_vz += Sample_x[i] * Sample_Y[i]
sredkvy = sredkvy/n
sredkvx = sredkvx/n
#Расчёт коэффициентов линейной регрессии
a = (n * sum_vz - sum(Sample_x) * sum(Sample_Y)) / ((n * sum_2) - sum(Sample_x) * sum(Sample_x))
b = sum(Sample_Y) / n - sum(Sample_x) / n * a
print('a =', a)
print('b=',b)
print("Уравнение линейной регрессии:")
print(f'y = {a}*x+{b}')
sample_calc = [a*Sample_x[i] + b for i in range(len(Sample_x))]
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10,8))
ax.set_title('Сравнение ист истинных и подсчитанных результатов')
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Год", fontsize=16)
ax.set_ylabel("Значение", fontsize=16)
plt.scatter(Sample_x[0], Sample_Y[0], s= 40, color = 'yellow', label = "Фактические значения")
for i in range(len(Sample_x)):
    plt.scatter(Sample_x[i], Sample_Y[i], s= 40, color = 'yellow')
plt.plot(Sample_x, sample_calc, color = 'blue', label='Значения функции ЛР')
ax.legend()
plt.show()

delta_ex = 0
delta_ost = 0
y_m = sum(Sample_Y)/len(sample_calc)
for i in range(len(sample_calc)):
    delta_ex += (sample_calc[i]-y_m)**2
    delta_ost += (sample_calc[i]-Sample_Y[i])**2
delta_ex = delta_ex/len(sample_calc)
delta_ost = delta_ost/len(sample_calc)
disp = sredkvy
F_kr = (len(Sample_Y)-2)*delta_ex/delta_ost
print("F_критическая:", F_kr)
Ftabl =4.96
print("F_табличные:", Ftabl)
print("Коэффиент детерминации:", delta_ex/disp)
E = [sample_calc[i] - Sample_Y[i] for i in range(len(sample_calc))]
print(E)
if F_kr > Ftabl:
    print("Fкрит > Ftable, регрессионная модель значима")
else:
    print("Fкрит < Ftable, регрессионная модель не информативна")
fig, ax = plt.subplots(figsize=(10,8))
plt.scatter(Sample_x[0], E[0], s= 40, color = 'red', label = "Значение остатка")
for i in range(len(E)):
    plt.scatter(Sample_x[i], E[i], s=40, color='red')
plt.style.use('dark_background')
ax.set_xlabel("Год, x", fontsize=16)
ax.grid(linestyle = "dashed", alpha = 0.7)
plt.title("График остатков")
plt.show()
SS1 = E[0]**2+E[1]**2+E[2]**2+E[3]**2
SS2 = E[8]**2+E[9]**2+E[10]**2+E[11]**2
print("SS1", SS1)
print("SS2", SS2)
F = SS2/SS1
print(f"F = SS2/SS1 = {F}")
Ftabl2 = 9.28
if F > Ftabl2:
    print("Fкрит > Ftable, статистическая гипотеза об одинаковой дисперсии возмущений отклоняется")
else:
    print("Fкрит < Ftable, гетероскедастичность не установлена")
norm_x = [1/Sample_x[i] for i in range(len(Sample_x))]
norm_y = [Sample_Y[i]/Sample_x[i] for i in range(len(Sample_x))]
norm_e = [E[i]/Sample_x[i] for i in range(len(Sample_x))]
print(norm_x)
print(norm_y)

n = len(Sample_x)
sum_vz = 0
sum_2 = 0
sredkvy = 0
sredkvx = 0
for i in range(n):
    sredkvx += (norm_x[i] - sum(norm_x) / n) ** 2
    sredkvy += (norm_y[i] - sum(norm_y) / n) ** 2
    sum_2 += norm_x[i] * norm_x[i]
    sum_vz += norm_x[i] * norm_y[i]
sredkvy = sredkvy/n
sredkvx = sredkvx/n
#Расчёт коэффициентов линейной регрессии
a = (n * sum_vz - sum(norm_x) * sum(norm_y)) / ((n * sum_2) - sum(norm_x) * sum(norm_x))
b = sum(norm_y) / n - sum(norm_x) / n * a
print('a =', a)
print('b=',b)
print("Уравнение линейной регрессии:")
print(f'y = {a}*x+{b}')
y_norm_calc = [a*norm_x[i]+b+norm_e[i] for i in range(len(sample_calc))]
print(y_norm_calc)
E = [y_norm_calc[i] - norm_y[i] for i in range(len(sample_calc))]
SS1 = E[0]**2+E[1]**2+E[2]**2+E[3]**2
SS2 = E[8]**2+E[9]**2+E[10]**2+E[11]**2
print("SS1", SS1)
print("SS2", SS2)
F = SS2/SS1
print(f"F = SS2/SS1 = {F}")