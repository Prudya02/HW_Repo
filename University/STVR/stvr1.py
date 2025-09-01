#VARIANT 7, a1 = 0.01; a2 = 0.05
import math
import numpy as np
import matplotlib.pyplot as plt


sample_june =[12.8, 12.9, 12.1, 12.4, 11.8,11.6,11.5,11.6, 12.3,11.9,11.6,12.2,11.4,10.8,11.8,10.5,10.7,11.5,10.5,
              11.1,11.8,11.1,10.5,11.5,11.3,11.2,10.6,11.5,11.0,11.4,11.9,10.8,11.5,11.5,12.7,11.2,10.4]
sample_july = [9.7, 9.5, 9.5, 9.3, 8.9, 9.3, 9.4, 10.1, 10, 10.5, 9.5, 9.8, 9.5, 9.5, 9.2, 9.4, 9.1, 8.7, 8.0, 9.4,
                  8.5, 7.9, 9.0, 9.1, 9.1, 9.1,9.5,8.9,8.9,8.8,9.0,9.7,9.0,9.7,9.0,9.7,8.5]
sample_august = [9.6, 9.6, 8.6, 8.4, 9.0, 8.9, 9.2, 9.3, 9.0,9.3,8.9,8.7,9.0, 9.5,9.0,8.4,8.8,8.6,8.5, 7.5, 8.0,7.0,8.0,
                   9.0,8.9,8.3,8.5,8.0,9.0,7.3,8.1,9.2,7.9,8.3,8.2,8.6,8.2]



plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10,8))
ax.set_title('Рисунок 1. Временная изменчивость температуры поверхности океана в июне, июле и августе.')
x = np.arange(1957, 1993+1)
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Года",fontsize=16)
ax.set_ylabel("темпрература воды, С",fontsize=16)
plt.plot(x, sample_june, label = 'Июнь')
plt.plot(x, sample_july, label = 'Июль')
plt.plot(x, sample_august, label = 'Август')
plt.plot(1957,6)
plt.plot(1957,13)
ax.legend()
plt.show()



sample_june_sorted = sample_june
sample_june_sorted.sort()
print("Вариационный ряд для температуры июня:")
print(sample_june_sorted)


plt.clf()
fig, ax = plt.subplots(figsize=(10,8))
plt.plot(sample_june_sorted, label ='отсортированный массив')
ax.set_xlabel("Индекс элемента",fontsize=16)
ax.set_ylabel("Значение элемента",fontsize=16)
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.hlines(sample_june_sorted[0], 0, 37, colors="blue", label='Экстремальные значения')
ax.hlines(sample_june_sorted[-1], 0, 37, colors ="blue")
plt.plot(0,13.5)
ax.legend()
plt.show()


n = 37
print("Объем выборки равен:", n)
print("Проверим, подчиняется ли заданная выборка нормальному распределению")
R = sample_june_sorted[-1] - sample_june_sorted[0]
print("Размах выборки R = ",R )
N = 1+int(math.log2(n))
print("Число интервалов разбиения найдем по формуле Стерджеса: 1+[log2(n)] =", N)
h = R/N
print("Величина интервалов = R/N =", h)
i = 0
borders = []
while i <= 6:
    borders.append(round(sample_june_sorted[0] + i * h, 4))
    i+=1
print("Точки разбиения интервалов", borders)
m = [0] * N
w = [0] * N
for i in range(N):
    for j in range(n):
        if sample_june_sorted[j]>=borders[i] and (sample_june_sorted[j] < borders[i + 1]):
            m[i]+=1
m[-1] += 1
for i in range(N):
    w[i] = m[i]/n
print("Абсолютные частоты:", m)
print("Относительные частоты:",w)
print('Проверяем условия нормировки для m:',sum(m), '==', n)
print('И для w:', sum(w),'==',1)
med_borders = []
for i in range(N):
    med_borders.append((borders[i]+borders[i+1])/2)
print('Середины интервалов:',med_borders)
plt.clf()
fig, ax = plt.subplots(figsize=(10,8))
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.vlines(med_borders[0], 0, m[0], color = 'r', label="Гистограмма")
for i in range (N):
    ax.vlines(med_borders[i], 0, m[i], color = 'r', linewidth =100)
plt.plot(med_borders, m, label="Полигон распределения")
ax.set_xlabel("Значение температуры, С",fontsize=16)
ax.set_ylabel("Частота",fontsize=16)
ax.legend()
plt.show()
x_sred = 0
x_kvadr = 0
for i in range(N):
    x_sred+=m[i]*med_borders[i]
x_sred = x_sred/n
print('Выборочное среднее равно', x_sred)
for i in range(N):
    x_kvadr+=m[i]*(med_borders[i]-x_sred)*(med_borders[i]-x_sred)
x_kvadr = x_kvadr/n
x_kvadr = np.sqrt(x_kvadr)
print('Выборочное среднее квадратическое отклонение равно ', x_kvadr)
print('Перейдем к нормированным величинам')
z = []
i = 1
z.append(-np.inf)
while i < N:
    z.append((borders[i]-x_sred)/x_kvadr)
    i+=1
z.append(np.inf)
print(z)
print('Вычислим Pi:')
P = []
P.append(-0.341+0.5)
P.append(-0.135+0.341)
P.append(0.122+0.135)      #таблично заданные (не было возможности подключить sсipy)
P.append(0.334-0.122)
P.append(0.4584-0.334)
P.append(0.5 - 0.4584)
print(P)
print("Вычислим теоретические чатосты:")
m2 = []
for i in range(N):
    m2.append(P[i]*n)
print(m2)
X_obs = 0
for i in range (N):
    X_obs+= (m[i]- m2[i])*(m[i]-m2[i])/m2[i]
print("Наблюдаемое значение критерия:", X_obs)
print("Число степеней свободы k = N-3 =", N-3)
a1 = 0.01
a2 = 0.05
Xkr1 = 11.345 #по таблице
Xkr2 = 7.815 #по таблице
if (X_obs < Xkr1):
    print("Для уровня значимости a = 0.01 гипотеза о нормальном рапределении исходной выборки может являться правдивой")
else:
    print("Для уровня значимости a = 0.01 гипотеза о нормальном рапределении исходной выборки является ложной")
if (X_obs < Xkr2):
    print("Для уровня значимости a = 0.05 гипотеза о нормальном рапределении исходной выборки может являться правдивой")
else:
    print("Для уровня значимости a = 0.05 гипотеза о нормальном рапределении исходной выборки является ложной")



#Если производить слияние интервалов
print("Слияние интервалов с недостаточным значением частоты:")
borders_new = [10.4, 10.8167, 11.2333, 11.65, 12.0667, 12.9]
N_new = 5
m_new = [8,5,12,5,7]
w_new = [0]*5
print("Границы новых интервалов:", borders_new)
print("Абсолютные частоты после слияния:",m_new)
for i in range(N_new):
    w_new[i] = m_new[i]/n
print("Соответствующие относительные частоты:", w_new)
med_borders_new =[]
for i in range(N_new):
    med_borders_new.append((borders_new[i]+borders_new[i+1])/2)
print('Середины новых интервалов:',med_borders_new)

plt.clf()
fig, ax = plt.subplots(figsize=(10,8))
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.vlines(med_borders_new[0], 0, m_new[0], color = 'r', label="Гистограмма")
for i in range (N_new):
    if i == N_new-1:
        ax.vlines(med_borders_new[i], 0, m_new[i], color='r', linewidth=170)
    else:
        ax.vlines(med_borders_new[i], 0, m_new[i], color = 'r', linewidth =85)
plt.plot(10.4,0)
plt.plot(12.9,0)
plt.plot(med_borders_new, m_new, label="Полигон распределения")
ax.set_xlabel("Значение температуры, С",fontsize=16)
ax.set_ylabel("Частота",fontsize=16)
ax.legend()
plt.show()
x_sred_new = 0
x_kvadr_new = 0
for i in range(N_new):
    x_sred_new+=m[i]*med_borders_new[i]
x_sred_new = x_sred_new/n
print('Выборочное среднее(новое) равно', x_sred_new)
for i in range(N_new):
    x_kvadr_new+=m_new[i]*(med_borders_new[i]-x_sred_new)*(med_borders_new[i]-x_sred_new)
x_kvadr_new = x_kvadr_new/n
x_kvadr_new = np.sqrt(x_kvadr_new)
print('Выборочное среднее квадратическое отклонение (новое) равно ', x_kvadr)
z_new = []
i = 1
z_new.append(-np.inf)
while i < N_new:
    z_new.append((borders_new[i]-x_sred_new)/x_kvadr_new)
    i+=1
z_new.append(np.inf)
print('Перейдем к нормированным величинам')
print(z_new)
print("Вычислим Pi после слияния:")
P_new = []
P_new.append(0.1217+0.5)
P_new.append(0.2453-0.1217)
P_new.append(0.341-0.2453)      #таблично заданные Pi после слияния интервалов
P_new.append(0.412-0.341)
P_new.append(0.5-0.412)
print(P_new)
print("Вычислим теоретические чатосты после слияния:")
m2_new = []
for i in range(N_new):
    m2_new.append(P_new[i]*n)
print(m2_new)
X_obs_new = 0
for i in range (N_new):
    X_obs_new+= (m_new[i]- m2_new[i])*(m_new[i]-m2_new[i])/m2_new[i]
print("Наблюдаемое значение критерия после слияния:", X_obs_new)
print("Число степеней свободы после слияния k_new = N_new-3 =", N_new-3)
Xkr1_new = 9.210 #по таблице
Xkr2_new = 5.991  #по таблице
if (X_obs_new < Xkr1_new):
    print("Для уровня значимости a = 0.01 гипотеза о нормальном рапределении исходной выборки может являться правдивой")
else:
    print("Для уровня значимости a = 0.01 гипотеза о нормальном рапределении исходной выборки является ложной")
if (X_obs_new < Xkr2_new):
    print("Для уровня значимости a = 0.05 гипотеза о нормальном рапределении исходной выборки может являться правдивой")
else:
    print("Для уровня значимости a = 0.05 гипотеза о нормальном рапределении исходной выборки является ложной")
