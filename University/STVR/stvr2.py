import numpy as np
import matplotlib.pyplot as plt
sample_1 = [12.8, 12.9, 12.1, 12.4, 11.8,11.6,11.5,11.6, 12.3,11.9,11.6,12.2,11.4,10.8,11.8,10.5,10.7,11.5,10.5,
            11.1,11.8,11.1,10.5,11.5,11.3,11.2,10.6,11.5,11.0,11.4,11.9,10.8,11.5,11.5,12.7,11.2,10.4]
sample_2 = [13.3,13.4,12.4,13.2,12.0,12.3,12.1,11.8,12.7,12.6,12.0,13.1,11.8,11.5,12.9,11.3,11.5,12.2,11.2,10.6,11.6,11.1,
            10.7,12.4,11.1,12.3,11.2,12.5,11.8,12.0,13.1,11.7,12.0,11.9,12.9,11.7,11.6]
sample_3 = [11.8,13.2,11.7,12.3,11.5,11.5,11.3,11.5,11.7,11.8,11.6,12.2,11.4,11.6,11.9,11.1,11.2,11.1,10.5,10.5,11.0,11.3,
            11.0,12.4,11.5,10.4,11.0,11.3,11.1,11.6,11.5,11.6,11.0,11.0,11.6,10.6,11.6]

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10,8))
ax.set_title('Значения 3-ех статистических рядов.')
x = np.arange(0, len(sample_1))
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Индекс ряда",fontsize=16)
ax.set_ylabel("Значения стат.ряда",fontsize=16)
plt.plot(x, sample_1, label = '1-ый ряд')
plt.plot(x, sample_2, label = '2-ой ряд')
plt.plot(x, sample_3, label = '3-ий ряд')
ax.legend()
plt.show()
sred_1 =  np.round(np.sum(sample_1) / len(sample_1), 4)
sred_2 = np.round(np.sum(sample_2) / len(sample_2), 4)
sred_3 = (np.sum(sample_3) / len(sample_1))
print("Выборочное среднее первого ряда:", sred_1)
print("Выборочное среднее второго ряда:", sred_2)
print("Выборочное среднее третьего ряда:", sred_3)
disp1, disp2, disp3, disp_fixed_1, disp_fixed_2, disp_fixed_3, Asimm1, Asimm2, Asimm3,Ex1, Ex2,Ex3 = [0 for i in range (12)]

for i in range(len(sample_1)):
    disp1 += (sample_1[i]-sred_1)*(sample_1[i]-sred_1)
    disp2 += (sample_2[i]-sred_2)*(sample_2[i]-sred_2)
    disp3 += (sample_3[i]-sred_3)*(sample_3[i]-sred_3)
    Asimm1 += (sample_1[i]-sred_1)*(sample_1[i]-sred_1)*(sample_1[i]-sred_1)
    Asimm2 += (sample_2[i]-sred_2)*(sample_2[i]-sred_2)*(sample_2[i]-sred_2)
    Asimm3 += (sample_3[i]-sred_3)*(sample_3[i]-sred_3)*(sample_3[i]-sred_3)
    Ex1 +=  (sample_1[i]-sred_1)*(sample_1[i]-sred_1)*(sample_1[i]-sred_1)*(sample_1[i]-sred_1)
    Ex2 += (sample_2[i]-sred_2)*(sample_2[i]-sred_2)*(sample_2[i]-sred_2)*(sample_2[i]-sred_2)
    Ex3 += (sample_3[i]-sred_3)*(sample_3[i]-sred_3)*(sample_3[i]-sred_3)*(sample_3[i]-sred_3)

disp_fixed_1 = disp1/(len(sample_1)-1)
disp_fixed_2 = disp2/(len(sample_1)-1)
disp_fixed_3 = disp3/(len(sample_1)-1)

disp1 = disp1/len(sample_1)
disp2 = disp2/len(sample_2)
disp3 = disp3/len(sample_3)

Asimm1 = Asimm1/(len(sample_1)*(np.sqrt(disp1))*disp1)
Asimm2 = Asimm2/(len(sample_2)*(np.sqrt(disp2))*disp2)
Asimm3 = Asimm3/(len(sample_3)*(np.sqrt(disp3))*disp3)

Ex1 = Ex1/(len(sample_1)*disp1*disp1)-3
Ex2 = Ex2/(len(sample_2)*disp2*disp2)-3
Ex3 = Ex3/(len(sample_3)*disp3*disp3)-3
Sorted1 = [0 for i in range (len(sample_1))]
Sorted2 = [0 for i in range (len(sample_1))]
Sorted3 = [0 for i in range (len(sample_1))]
for i in range(len(sample_1)):
    Sorted1[i] = sample_1[i]
    Sorted2[i] = sample_2[i]
    Sorted3[i] = sample_3[i]
Sorted1.sort()
Sorted2.sort()
Sorted3.sort()
if len(sample_1)%2 == 0:
    Med1 = (Sorted1[int(len(sample_1)/2-1)]+Sorted1[int(len(sample_1)/2)])/2
    Med2 = (Sorted2[int(len(sample_2)/2-1)]+Sorted2[int(len(sample_2)/2)])/2
    Med3 = (Sorted3[int(len(sample_3) / 2 - 1)] + Sorted3[int(len(sample_3) / 2)])/2
else:
    Med1 = Sorted1[int((len(sample_1)-1)/2)]
    Med2 = Sorted2[int((len(sample_2) - 1) / 2)]
    Med3 = Sorted3[int((len(sample_3)-1)/2)]
print("\nВыборочная дисперсия для первого ряда:", disp1)
print("Выборочная дисперсия для второго ряда:", disp2)
print("Выборочная дисперсия для третьего ряда:", disp3)
print("\nИсправленная выборочная дисперсия для первого ряда:", disp_fixed_1)
print("Исправленная выборочная дисперсия для второго ряда:", disp_fixed_2)
print("Исправленная выборочная дисперсия для третьего ряда:", disp_fixed_3)
print("\nСтандартное отклонение для первого ряда:", np.sqrt(disp1))
print("Стандартное отклонение для второго ряда:", np.sqrt(disp2))
print("Стандартное отклонение для третьего ряда:", np.sqrt(disp3))
print("\nКоэффициент вариации для первого ряда", np.sqrt(disp1)/sred_1)
print("Коэффициент вариации для второго ряда", np.sqrt(disp2)/sred_2)
print("Коэффициент вариации для третьего ряда", np.sqrt(disp3)/sred_3)
print("Для трех рядов характерна высокая степень концентрации относительно среднего")
print("\nКоэффициент ассиметрии для первого ряда", Asimm1)
print("Коэффициент ассиметрии для второго ряда", Asimm2)
print("Коэффициент ассиметрии для третьего ряда", Asimm3)
print(" Для первых двух рядов характерна умеренная асимметрия, для третьего - большая;  для первого рядараспределение скошено вправо; для второго и третьего – распределение скошено влево.")
print("\nКоэффициент эксцесса для первого ряда", Ex1 )
print("Коэффициент эксцесса для второго ряда", Ex2 )
print("Коэффициент эксцесса для третьего ряда", Ex3 )
print("Эмпирические кривые распределений приближены к нормальному; для второго и третьего ряда распределение имеет острый пик; для первого – распределение имеет плосковершинную форму.")
print("\nМедиана для первого ряда", Med1)
print("Медиана для второго ряда", Med2)
print("Медиана для третьего ряда", Med3)
print("Мода для первого ряда", 11.5)
print("Мода для второго ряда", 9.5)
print("Мода для третьего ряда", 9.0)
print("Моды и медианы для всех рядов довольно схожи, что может свидетельствовать о нормальном распределении данных рядов")
