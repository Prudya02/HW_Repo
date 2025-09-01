import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import scipy.special
import seaborn as sns
import math
from sympy.abc import a, x, y
from sympy import init_printing
from itertools import combinations
#R4
def R_2(D, a, b, t):
    return D * np.exp(-a * np.abs(t)) * (np.cos(b*t)+a/b*np.sin(b*np.abs(t)))
#R14
def R_1(D, a, t):
    return D * np.exp(-1*(a * t)**3)

def gamma_1(D, a, t):
    return R_1(D, a, 0) - R_1(D, a, t)

def gamma_2(D, a, b, t):
    return R_2(D, a, b, 0) - R_2(D, a, b, t)

def t11(a):
    return scipy.special.gamma(4/3)/a
def t12(D,a):
    return np.abs(D)*scipy.special.gamma(4/3)/(a*D)
def t13(D,a):
    return scipy.special.gamma(4/3)/(2**(1/3)*a)

def f01(D, a):
    return D/(2*a*np.sqrt(np.pi))

def f02(D,a,b):
    return 2*a*D/(a**2+b**2)
def gamma_emp(h, mas):
    sum = 0
    for i in range(len(mas)-h):
        sum += (mas[i+h]-mas[i])**2
    sum /= (2*(len(mas)-h))
    return sum

def R_emp(h, mas):
    summa = 0
    sred = sum(mas)/len(mas)
    for i in range(len(mas)-h):
        summa = summa + (mas[i+h]-sred)*(mas[i]-sred)
    summa = summa/(len(mas)-h)
    return summa
def superplots_1(func):
    fig, axes = plt.subplots(3, 3, figsize=(16, 14))
    D = [1, 9, 25]
    A = [0.1, 1.5, 4]
    X = np.linspace(0, 10, 1000)

    for i, d in enumerate(D):
        for j, a in enumerate(A):
            Y = func(d, a, X)
            sns.lineplot(x=X, y=Y, ax=axes[j, i])
            axes[j, i].set_title(f'D = {d}, a = {a}')

def f14(D, a, lamb):
    return (D/2*a*math.sqrt(np.pi))*np.exp(-(lamb/2*a)**2)
def superplots_2(func):
    fig, axes = plt.subplots(4, 2, figsize=(16, 24))
    D = [1, 16]
    A = [0.1, 2]
    B = [0.4, 1]
    X = np.linspace(0, 10, 1000)
    for i, d in enumerate(D):
        for j, a in enumerate(A):
            Y = func(d, a, B[0], X)
            sns.lineplot(x=X, y=Y, ax=axes[j, i])
            axes[j, i].set_title(f'D = {d}, a = {a}, b = {B[0]}')
            # axes[j, i].set_xlim(0, 10)

    for i, d in enumerate(D):
        for j, a in enumerate(A):
            Y = func(d, a, B[1], X)
            sns.lineplot(x=X, y=Y, ax=axes[j + 2, i])
            axes[j + 2, i].set_title(f'D = {d}, a = {a}, b = {B[1]}')
            # axes[j, i].set_xlim(0, 10)
plt.style.use('dark_background')
superplots_1(R_1)
plt.suptitle('R_14(t)', fontsize=20)
plt.show()
print("Класс R_14: монотонно убывающий")
superplots_2(R_2)
plt.suptitle('R_4(t)', fontsize=20)
plt.show()
print("Класс R_4: колебательный")
superplots_1(gamma_1)
plt.suptitle('Семивар. R_14(t)', fontsize=20)
plt.tight_layout(pad=3)
plt.show()
superplots_2(gamma_2)
plt.suptitle('Семивар. R_4(t)', fontsize=20)
plt.tight_layout(pad=3)
plt.show()
A = [0.1, 1.5, 4]
D = [1, 16]
B = [0.4, 1]
L14 = D[0]/(2*f01(D[0], A[0]))
L4 = D[0]/(2*f02(D[0], A[0], B[0]))
f_arr =[]
for i in range(-50, 50):
   f_arr.append(f14(D[0], A[0], i))
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10,8))
ax.set_title('Спектральная плотонсть для R(14)')
x = np.arange(-50, 50)
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Значеніе lambda",fontsize=16)
ax.set_ylabel("Значения плотності",fontsize=16)
plt.plot(x, f_arr, label = 'плотность')
plt.show()

print(f"Для R_14 (a = 0.1): t0(1) = {t11(A[0])}, t0(2) = {t12(D[0],A[0])}, t0(3) = {t13(D[0],A[0])}")
print("L Для R_14(a = 0.1, D - сократится)): ", L14)
print("L Для R_4(a = 0.1,b = 0.4, D - сократится)): ", L4)
print(f"Проверим нер-во неопределенности для R_14: {t12(D[0],A[0])}*{L14} = {t12(D[0],A[0])*L14} > {np.pi/2}")




April = [10.5, 4, 4, 4, 8.5, 3.5, 3, 2, 7, 12.5, 15.5, 15.5, 15, 7.5, 6.5, 10.5, 11, 14.5, 12, 6.5, 12.5, 8.5, 5, 3.5, 3.5, 3, 4, 5.5, 12.5, 12.5]
Years = [-9.9, -3.3, 2.9, 12.6, 17.4, 21.4, 25.4, 25.3, 14.6, 7.6, 4.6, -6.2,
         -3.35, -5.78, 3.2, 9.8, 16.3, 19.4, 22, 23.1, 16, 5.1, 3.0, -5.3,
         -7.0, -2.8, 5, 12.1, 18.3, 15.9, 24.9, 24.2, 15.1, 9.6, 4.3, -7,
         -8.6, -2.2, 3.0, 12.3, 13.4, 14.5, 22.1, 23.3, 15.6, 12.4, 3.4, -4]
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10,8))
ax.set_title('Cреднесуточная температура в апреле 2021')
x = np.arange(0, len(April))
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("День месяца",fontsize=16)
ax.set_ylabel("Значения температуры",fontsize=16)
plt.plot(x, April, label = 'температура в апреле')
plt.show()
ax.set_title('Гистограмма температуры в апреле 2021')
ax.set_xlabel("Значения температур",fontsize=16)
ax.set_ylabel("Частота",fontsize=16)
plt.hist(April, density = True, bins = 5)
plt.show()
fig, ax = plt.subplots(figsize=(10,8))
ax.set_title('Cреднемесячная температура в 2010-2013')
x = np.arange(0, len(Years))
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Месяц от янв. 2010",fontsize=16)
ax.set_ylabel("Значения средней температуры",fontsize=16)
plt.plot(x, Years)
plt.show()
ax.set_title('Гистограмма температуры в 2010-2013')
ax.set_xlabel("Значения температур",fontsize=16)
ax.set_ylabel("Частота",fontsize=16)
plt.hist(April, density = True, bins = 7)
plt.show()
print("ПРОВЕРКА ПЕРВОГО РЯДА НА ТРЕНД:")
sample_sort = April.copy()
sample_sort = sorted(sample_sort)
median = sample_sort[int((len(sample_sort)-1)/2)]
plus_minus =  April.copy()
plus_minus2 = April.copy()
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
T = len(April)
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
print("ПРОВЕРКА ВТОРОГО РЯДА НА ТРЕНД:")
sample_sort = Years.copy()
sample_sort = sorted(sample_sort)
median = sample_sort[int((len(sample_sort)-1)/2)]
plus_minus = Years.copy()
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
T = len(Years)
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



def Y1(C,a,h):
    return C*(1-np.exp(-h/a))


def Y2(C,a,h):
    return C*(1-np.exp(-h/a))


gamma_emp1 = []
r_emp1 = []
gamma_model1 = []
gamma_emp2 = []
r_emp2 = []
for i in range(20):
    gamma_model1.append(Y1(24,2.2,i))
    r_emp1.append(R_emp(i,April))
    gamma_emp1.append(gamma_emp(i, April))
for i in range(36):
    r_emp2.append(R_emp(i, Years))
    gamma_emp2.append(gamma_emp(i, Years))
#print("ОЦЕНКА СЕМИВАРИОГРАММЫ ДЛЯ 1-ОГО РЯДА:")
#print(gamma_emp1)
#print("ОЦЕНКА СЕМИВАРИОГРАММЫ ДЛЯ 2-ОГО РЯДА:")
#print(gamma_emp2)
print("Оценка Ковариации для 1-ого ряда:")
print(r_emp1)
print("Оценка Ковариации для 2-ого ряда:")
print(r_emp2)

fig, ax = plt.subplots(figsize=(10,8))
ax.set_title('Графики оценок семивариограммы и ковариации для 1-го ряда')
x = np.arange(0, 20)
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Длина лага ",fontsize=16)
ax.set_ylabel("Значения оценок",fontsize=16)
plt.plot(x, gamma_model1, label ="Модель семивариограммы")
plt.plot(x, gamma_emp1, label = "Оценка семивариограммы")
plt.plot(x, r_emp1, label = "Оценка ковариации")
ax.legend()
plt.show()
fig, ax = plt.subplots(figsize=(10,8))
x = np.arange(0, 36)
ax.set_title('Графики оценок семивариограммы и ковариации для 2-го ряда')
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Длина лага ",fontsize=16)
ax.set_ylabel("Значения оценок",fontsize=16)
plt.plot(x, gamma_emp2, label = "Оценка семивариограммы")
plt.plot(x, r_emp2, label = "Оценка ковариации")
ax.legend()
plt.show()
