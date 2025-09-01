import math
import numpy as np
import matplotlib.pyplot as plt
sample_3 = [11.8,13.2,11.7,12.3,11.5,11.5,11.3,11.5,11.7,11.8,11.6,12.2,11.4,11.6,11.9,11.1,11.2,11.1,10.5,10.5,11.0,11.3,
            11.0,12.4,11.5,10.4,11.0,11.3,11.1,11.6,11.5,11.6,11.0,11.0,11.6,10.6,11.6]
sample_sort = sample_3.copy()
sample_sort = sorted(sample_sort)
median = sample_sort[int((len(sample_sort)-1)/2)]
plus_minus = sample_3.copy()
plus_minus2 = sample_3.copy()
i = 0
longest = 0
length = 1
prev = 2
count = 0
while i < len(plus_minus):
    if plus_minus[i] > median:
        plus_minus[i] = 1
        if prev == 1:
            length += 1
        else:
            if length > longest:
                longest = length
            length = 1
            count += 1
        prev = 1
    elif plus_minus[i] < median:
        plus_minus[i] = 0
        if prev == 0:
            length += 1
        else:
            if length > longest:
                longest = length
            length = 1
            count += 1
        prev = 0
    else:
        plus_minus.pop(i)
        i -= 1
    i += 1
print("Метод серий, основанный на медиане")
print("Медиана:", median)
print(plus_minus)
T = len(sample_3)
print("Максимальная длина последовательности l(T):", longest)
print("Общее число серий nu(T):", count)
if count < 0.5*(T+1-1.96*math.sqrt(T-1)):
    print(count, "<", 0.5*(T+1-1.96*math.sqrt(T-1)), "с вероятностью 95% тренд существует")
else:
    print(count, ">", 0.5*(T+1-1.96*math.sqrt(T-1)))
if longest > math.log2(T+1):
    print(longest, ">", math.log2(T+1), "с вероятностью 95% тренд существует")
else:
    print(longest, "<", math.log2(T + 1))
if count >= 0.5*(T+1-1.96*math.sqrt(T-1)) and longest <= math.log2(T+1):
    print("Нельзя сделать вывод о наличии тренда, пользуям методом серии, основанном на медиане")
print("\nМетод восходящих и нисходящих серий")
count = 1
length = 0
longest = 0
for i in range(len(plus_minus2)-1):
    if plus_minus2[i] < sample_3[i+1]:
        plus_minus2[i] = 1
        if prev == 1:
            length += 1
        else:
            if length > longest:
                longest = length
            length = 1
            count += 1
        prev = 1
    elif plus_minus2[i] > sample_3[i+1]:
        plus_minus2[i] = 0
        if prev == 0:
            length += 1
        else:
            if length > longest:
                longest = length
            length = 1
            count += 1
        prev = 0
    else:
        plus_minus2[i] = prev
        length += 1
plus_minus2.pop()
print(plus_minus2)
print("Максимальная длина последовательности l(T):", longest)
print("Общее число серий nu(T):", count)
if count < (1/3)*(2*T-1) - 1.96*math.sqrt((16*T-29)/90):
    print(count, "<", (1/3)*(2*T-1) - 1.96*math.sqrt((16*T-29)/90), "с вероятностью 95% тренд существует")
else:
    print(count, ">", (1 / 3) * (2 * T - 1) - 1.96 * math.sqrt((16 * T - 29) / 90))
if longest > 6:
    print(longest, ">", math.log2(T + 1), "с вероятностью 95% тренд существует")
else:
    print(longest, "<", math.log2(T + 1))
if count >= (1/3)*(2*T-1) - 1.96*math.sqrt((16*T-29)/90) and longest <= 6:
    print("Нельзя сделать вывод о наличии тренда, пользуям методом восходящих и нисходящих серий")
print("\nСглаживание способом скользящей средней")

m = 3
new_arr = [0 for i in range(len(sample_3)-2*m)]
for i in range(m, T-m):
    sum1 = 0
    for l in range(-m, m+1):
        sum1 += sample_3[i+l]
    sum1 = sum1/(2*m+1)
    new_arr[i-m] = sum1
print(new_arr)
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10,8))
ax.set_title('Сравнение ист истинных и сглаженных результатов')
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Год", fontsize=16)
ax.set_ylabel("Значение", fontsize=16)
x = np.arange(1957, 1994)
x2 = np.arange(1957+m, 1994-m)
plt.plot(x, sample_3, label='Фактические значения')
plt.plot(x2, new_arr, color = 'blue', label='Сглаженные значения')
ax.legend()
plt.show()
print("Линейное уравнение модели тренда:")
T = len(new_arr)
sum1 = 0
sum2 = 0
mid = 1975
for i in range(int(-(T-1)/2), int((T-1)/2)+1):
    sum1 += i*new_arr[i+int((T-1)/2)]
    sum2 += i*i
a = sum1/sum2
b = sum(new_arr)/T
T = np.linspace(int(-(T-1)/2), int((T-1)/2)+1, 31)
sample_calc = [a*T[i]+b for i in range(len(T))]
print(sample_calc)
print(f'y*(t) = {a}*t + {b}')
print("\nРассчитаем коэффициент корелляции")
sy = sum(new_arr)/len(T)
st = sum(sample_calc)/len(T)
srkvt = 0
srkvy = 0
srkvty = 0
for i in range(len(T)):
    srkvt += (sample_calc[i] - st)**2
    srkvy += (new_arr[i] - sy) ** 2
    srkvty += (sample_calc[i] - st)*(new_arr[i] - sy)
srkvty = srkvty/len(T)
srkvt = math.sqrt(srkvt / (len(T)))
srkvy = math.sqrt(srkvy / (len(T)))
r = srkvty/(srkvt*srkvy)
print("Коэффициент корелляции Rty = ", r)
delta_r = np.sqrt((1-r*r)/(len(T)-2))
print("Cреднеквадратическая ошибка коэффициента корреляции:", delta_r)
delta_ex = 0
delta_ost = 0
y_m = sum(new_arr)/len(T)
for i in range(len(sample_calc)):
    delta_ex += (sample_calc[i]-y_m)**2
    delta_ost += (sample_calc[i]-new_arr[i])**2
delta_ex = delta_ex/len(sample_calc)
delta_ost = delta_ost/len(sample_calc)
disp = srkvy**2
print("Коэффиент детерминации:", delta_ex/disp)
print("Коэффициент n < 0.7, модель не обладает должным уровнем приближения")
t_rasch = r/delta_r
t = 2.04
if t_rasch > t:
    print(t_rasch, " > ", t, "Тренд вносит определенный вклад в формирование изменчивости исходного ряда")

print("Дисперсия отклонения:", disp*(1-r*r))
plt.plot(x2, sample_calc, label='Тренд')
plt.plot(x2, new_arr, color = 'blue', label='Сглаженные значения')
plt.show()
print("Величина тренда в 1995 году:", a*(1995-mid)+b)
print("Характер тренда - отрицательный. ")