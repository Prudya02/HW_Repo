import numpy as np
import matplotlib.pyplot as plt
a = 0.5106309915581516
b = 5.281456574617395
sample_2 = [13.3, 13.4, 12.4, 13.2, 12.0, 12.3, 12.1, 11.8,12.7,12.6,12.0,13.1,11.8,11.5,12.9,11.3,11.5,12.2,11.2,10.6,11.6,11.1,
            10.7,12.4,11.1,12.3,11.2,12.5,11.8,12.0,13.1,11.7,12.0,11.9,12.9,11.7,11.6]
sample_3 = [11.8,13.2,11.7,12.3,11.5,11.5,11.3,11.5,11.7,11.8,11.6,12.2,11.4,11.6,11.9,11.1,11.2,11.1,10.5,10.5,11.0,11.3,
            11.0,12.4,11.5,10.4,11.0,11.3,11.1,11.6,11.5,11.6,11.0,11.0,11.6,10.6,11.6]
sample_calc = [a*sample_2[i]+b for i in range(len(sample_2))]
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10,8))
ax.set_title('Сравнение ист истинных результатов и регр.модели')
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Год", fontsize=16)
ax.set_ylabel("Значение", fontsize=16)
x = np.arange(1957, 1993+1)
print(len(x))
plt.plot(x, sample_3, label='Фактические значения')
plt.plot(x, sample_calc, color = 'blue', label='Рассчитанные значения')
ax.legend()
plt.show()
y_m = sum(sample_3)/len(sample_calc)
print("y_m = ", y_m)
delta_ex = 0
delta_ost = 0
disp = 0.2999269539810082
for i in range(len(sample_calc)):
    delta_ex += (sample_calc[i]-y_m)**2
    delta_ost += (sample_calc[i]-sample_3[i])**2
delta_ex = delta_ex/len(sample_calc)
delta_ost = delta_ost/len(sample_calc)
print("Объясненная дисперсия delta_sq =", delta_ex)
print("Остаточная дисперсия delta_ost =", delta_ost)
n = delta_ex/disp
print("Выборочная дисперсия:", disp)
r = 0.6662009037066482
print("Коэффициент детерминации", n)
print("n^2-Rxy^2 = ", n*n - r*r)
if abs(n*n - r*r) > 0.1:
    print("Отклонения от линейности выражены довольно сильно")
else:
    print("Отклонения от линейности несущественны")
F_kr = (len(sample_3)-2)*delta_ex/delta_ost
v1 = 1
v2 = 35
a = 0.05
F_table = 4.12
print("Fкрит = ", F_kr)
print("Fтабл = ", F_table)
if F_kr > F_table:
    print("Fкрит > Ftable, регрессионная модель значима")
else:
    print("Fкрит < Ftable, регрессионная модель не информативна")
