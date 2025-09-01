import scipy as sp
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats
n = 150
gamma0 = 1
gamma = 1
D = 1
p = np.exp(-gamma)
alpha0 = p*(p*p-1)*np.cos(gamma0)+gamma/gamma0*(1+p*p)*p*np.sin(gamma0)
alpha1 = 1-p*p*p*p-4*p*p*gamma/gamma0*np.sin(gamma0)*np.cos(gamma0)
a0 = np.sqrt(D*(alpha1*alpha1+np.sqrt(alpha1*alpha1-4*alpha0*alpha0))/2)
a1 = np.sqrt(D)*alpha0/alpha1
b1 = 2*p*np.cos(gamma0)
b2 = -p*p
#X_white = np.random.normal(0, 1, n) #белый шум
X_white = [-4.12496164e-01, -9.56227503e-01, -1.04127088e+00, -5.24766750e-01,
 -2.66847465e-01, -9.27568825e-01,  6.50708791e-01, -1.39470180e+00,
 -1.13560574e+00,  3.52236236e-01, -7.00376937e-01, -1.24307659e+00,
 -1.12815216e+00, -4.74795675e-01,  5.44918476e-01,  2.50724416e-01,
 -9.53437980e-01, -5.42468762e-01,  1.39900216e+00, -2.10453088e-01,
 -9.34333382e-01,  9.14941361e-01,  1.16411741e-01,  4.90495665e-01,
  9.45035452e-01,  1.12006818e+00,  4.19576046e-01, -3.97025527e-01,
 -3.22414083e-01, -1.38656984e+00, -1.00927021e+00,  9.90256837e-01,
 -7.70237228e-01, -1.00318316e-01, -1.71925855e-01, -1.47940802e-01,
 -1.24758020e+00,  4.01379089e-01, -3.69438071e-01,  2.12345759e-01,
 -1.55052639e+00,  1.51893561e+00,  2.29912949e-01,  5.54456597e-01,
 -3.46273277e-01,  2.08475119e+00,  9.71095624e-01,  1.91245777e+00,
  1.42822050e-01, -1.04304200e+00,  1.63442957e+00,  1.17850856e+00,
 -1.45641706e+00,  1.37529847e+00,  3.20126948e-01, -1.58629826e-01,
  6.75486258e-01, -1.19091300e+00, -3.47603144e-01, -2.92517117e-01,
  2.36178005e-01, -2.98724131e-01, -3.86632826e-01,  8.37351072e-01,
 -5.23194684e-01,  5.99970743e-01,  1.67974941e+00,  8.55816325e-01,
 -6.67599233e-01, -1.36373042e-01,-2.84625059e+00, -1.04016514e-01,
  1.91920932e-01, -2.00589294e+00,  5.62089350e-01,  1.74116842e+00,
  1.26430699e+00, -1.20269227e+00,  8.76643136e-01, -2.83911673e-01,
 -6.14309210e-01, -6.01399068e-01, -9.48996020e-01, -1.34305982e+00,
 -8.03182501e-01, -6.53977952e-01, -1.14288295e+00, -4.29747977e-01,
  6.67102880e-01, -1.04963954e+00, -4.52266850e-01,  9.67004063e-02,
  1.93604152e+00,  6.66300263e-01, -6.70130136e-01,  1.20126575e+00,
  2.37167655e+00, -1.23067057e+00,  8.70081691e-01, -4.85734262e-01,
  6.53094561e-01, -2.35948100e-03,  1.14368938e+00, -4.21549829e-01,
  1.79445173e-01,  5.45742980e-01,  3.30957490e-01,  8.21225861e-01,
  8.03979808e-01,  5.30141814e-01, -1.26898847e+00,  1.98245251e-01,
  1.36788606e+00,  8.62170180e-01, -3.52344679e-01,  8.51768162e-01,
 -1.49265581e+00,  1.18580990e+00, -1.61785173e+00,  2.07147963e-01,
  1.45215172e-01,  9.98583973e-01, -1.60924910e+00,  6.12602301e-02,
  2.83107594e-01,  9.60214563e-01,  2.59504519e-01, -4.47374278e-01,
  2.08223435e+00,  3.06912622e-03,  5.97801994e-01, -5.64775453e-01,
 -5.99582072e-01, -6.03724093e-01, -1.40900170e+00,-1.72804469e+00,
 -7.25294223e-01, -1.45512990e+00, -1.65630185e+00,  3.39734870e-01,
  1.13633711e+00, -7.22007905e-01, -8.60318048e-01, -8.77597723e-01,
  9.34498670e-02,  3.52010122e-01,  1.86627668e+00, -1.43612928e+00,
 -1.04741973e+00,  6.75553690e-01] #Задали белый шум для примера
X_NEW = X_white
for i in range(2, n):
    X_NEW[i] = a0*X_white[i]+a1*X_white[i-1]+b1*X_NEW[i-1]+b2*X_NEW[i-2]
#2.График отсчётов
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10,8))
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Номер отсчёта",fontsize=16)
ax.set_ylabel("Значение",fontsize=16)
T = np.arange(1,n+1)
plt.plot(T, X_NEW, label = 'Отсчёты')
plt.show()
#3.Статистический анализ
nu_emp = sum(X_NEW)/n
print("Среднее выборочное:", nu_emp)
print("Медиана:", sorted(X_NEW)[int(len(X_NEW)/2)])
print(X_NEW)
#Проверка гипотезы на нормальность
sample_sorted = [0]*n
for i in range (n):
    sample_sorted[i] = X_NEW[i]
sample_sorted.sort()
print("Проверим, подчиняется ли заданная выборка нормальному распределению")
R_emp = sample_sorted[-1] - sample_sorted[0]
print("Размах выборки R = ", R_emp)
N = 1+int(math.log2(n))
print("Число интервалов разбиения найдем по формуле Стерджеса: 1+[log2(n)] =", N)
h = R_emp / N
print("Величина интервалов = R/N =", h)
i = 0
borders = []
while i <= N:
    borders.append(sample_sorted[0] + i * h)
    i+=1
print("Точки разбиения интервалов", borders)
m = [0] * N
w = [0] * N
for i in range(N):
    for j in range(n):
        if (sample_sorted[j]>=borders[i]) and (sample_sorted[j] < borders[i + 1]):
            m[i]+=1
for i in range(n):
    if sample_sorted[i] >= borders[-1]:
        m[-1]+=1
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
    ax.vlines(med_borders[i], 0, m[i], color = 'r', linewidth =1000/np.sqrt(n))
plt.plot(med_borders, m, label="Полигон распределения")
ax.set_xlabel("Значение отсчёта",fontsize=16)
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
P = [0 for i in range(N)]
for i in range(N):
    P[i] = (scipy.stats.norm.cdf(z[i+1])-0.5)-(scipy.stats.norm.cdf(z[i])-0.5)
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
Xkr1 = 4.032 #по таблице
Xkr2 = 2.571 #по таблице
if (X_obs < Xkr1):
    print("Для уровня значимости a = 0.01 гипотеза о нормальном рапределении исходной выборки может являться правдивой")
else:
    print("Для уровня значимости a = 0.01 гипотеза о нормальном рапределении исходной выборки является ложной")
if (X_obs < Xkr2):
    print("Для уровня значимости a = 0.05 гипотеза о нормальном рапределении исходной выборки может являться правдивой")
else:
    print("Для уровня значимости a = 0.05 гипотеза о нормальном рапределении исходной выборки является ложной")
#4.Оценка ковариационной функции.
R = [0 for i in range(int(n*2/3))]
R_emp = [0 for i in range(int(n*2/3))]
for i in range(int(n*2/3)):
    R[i] = D*np.exp(-i*gamma)*(np.cos(gamma0*i)+gamma/gamma0*np.sin(gamma0*i))
for h in range (int(n*2/3)):
    sum = 0
    for s in range (1, n-h):
        sum+=(X_NEW[s+h-1]-nu_emp)*(X_NEW[s-1]-nu_emp)
    print(sum)
    R_emp[h] = sum / (n - h)
print(R_emp)
ax.set_xlabel("Значение шага h",fontsize=16)
ax.set_ylabel("Значение ков.функции",fontsize=16)
T = np.arange(0, n*2/3)
plt.plot(T, R_emp, label ='оценка ков.функцци')
plt.plot(T, R, label = 'ковариационная функция')
plt.show()