
#В4.  n = 30, 50, 75, 100, 125, 150, 200, 250, 300, 350; h = 2, 9, 18.
import scipy as scipy
import scipy.stats
import scipy.special
import numpy as np
import matplotlib.pyplot as plt

def R_2(D, a, b, t):
     return D * np.exp(-a * np.abs(t)) * (np.cos(b * t) + a / b * np.sin(b * np.abs(t)))

def gamma_2(D, a, b, t):
    return R_2(D, a, b, 0) - R_2(D, a, b, t)

def gamma_class(h, mas):
    sum = 0
    for i in range(len(mas) - h):
        sum += (mas[i + h] - mas[i]) ** 2
    sum /= (2 * (len(mas) - h))
    return sum

def gamma_rob(h,mas):
    sum = 0
    for i in range(len(mas) - h):
        sum += np.abs((mas[i + h] - mas[i])) ** (1 / 2)
    sum /= (len(mas) - h)
    sum = sum**4
    sum = sum/(2*(0.457+0.494/(len(mas)-h)+0.045/(len(mas)-h)**2))
    return sum


n = 100
gamma0 = 1
gamma = 1
D = 3
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
X_NEW = X_white[:n]
for i in range(2, n):
    X_NEW[i] = a0*X_white[i]+a1*X_white[i-1]+b1*X_NEW[i-1]+b2*X_NEW[i-2]
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10,8))
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Номер отсчёта",fontsize=16)
ax.set_ylabel("Значение",fontsize=16)
T = np.arange(1,n+1)
plt.plot(T, X_NEW, label = 'Отсчёты')
plt.show()
R_arr = []
Gamma_arr = []
Gamma_emp_class = []
Gamma_emp_rob = []
Gamma_arr_big = []
Gamma_arr_big2 = []
for i in range(100):
    Gamma_arr.append(gamma_2(D,gamma0,gamma,i/10))
    R_arr.append(R_2(D,gamma0,gamma,i/10))
    Gamma_arr_big.append(gamma_2(D,gamma0,gamma,i/2))
    Gamma_arr_big2.append(gamma_2(D,gamma0,gamma,i))
fig, ax = plt.subplots(figsize=(10,8))
plt.style.use('dark_background')
plt.title("Значение ков.функции и семивариограммы",fontsize=16)
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Время t, 0.1 лага",fontsize=16)
ax.set_ylabel("Значение",fontsize=16)
T = np.arange(0,100)
plt.plot(T, R_arr, label = 'Ков.функция')
plt.plot(T, Gamma_arr, label = 'Семивариограмма')
ax.legend()
plt.show()
for i in range(50):
    Gamma_emp_class.append(gamma_class(i, X_NEW))
    Gamma_emp_rob.append(gamma_rob(i, X_NEW))
fig, ax = plt.subplots(figsize=(10,8))
plt.style.use('dark_background')
plt.title("Значение оценок семивариограммы",fontsize=16)
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Величина лага",fontsize=16)
ax.set_ylabel("Значение семивариограммы",fontsize=16)
T = np.arange(0,50)
T2 = np.linspace(0,50,100)
plt.plot(T, Gamma_emp_class, label = 'Классическая оценка')
plt.plot(T, Gamma_emp_rob, label = 'Робастная оценка')
plt.plot(T2, Gamma_arr_big, label = 'Семивариограмма')
ax.legend()
plt.show()

subs_class = [Gamma_arr_big2[i] - Gamma_emp_class[i] for i in range(50)]
subs_rob = [Gamma_arr_big2[i] - Gamma_emp_rob[i] for i in range(50)]

fig, ax = plt.subplots(figsize=(10,8))
plt.style.use('dark_background')
plt.title("Остатки оценок семивариограммы",fontsize=16)
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Величина лага",fontsize=16)
ax.set_ylabel("Значение остатка",fontsize=16)
T = np.arange(0, 50)
plt.scatter(T[0], subs_class[0], s = 40, color = 'red', label = 'Классическая оценка')
plt.scatter(T[0], subs_rob[0], s = 40, color = 'yellow', label = 'Робастная оценка')
plt.hlines(0,0, 50, color = 'white')
plt.plot(0, D)
plt.plot(0, -D)
for i in range(50):
    plt.scatter(T[i], subs_class[i], s = 40, color = 'red')
    plt.vlines(T[i],0, subs_class[i], color = 'red')
    plt.scatter(T[i], subs_rob[i], s = 40, color = 'yellow', alpha=0.7)
    plt.vlines(T[i], 0, subs_rob[i], color='yellow', alpha = 0.7)
ax.legend()
plt.show()
#X_white = np.random.normal(0, 1, n) #белый шум
Disp_class = [[0.9686087139135215, 1.663865501343926, 2.2271194182948197], [0.5728987868323872, 0.9280537765462921, 1.0396528803624279],
              [0.37918385650287784, 0.59525379676917, 0.6456750102903976], [0.2833593021393026, 0.43784478675023564, 0.4656442099012376],
              [0.2261943753181237, 0.3462143147615098, 0.3637160648369585], [0.18822163397689573, 0.2862797122772013, 0.2982884977766785],
              [0.14090987153132098, 0.2126383936977431, 0.21929011904196183], [0.11260494498565753, 0.16912579881874268, 0.1733455897189129],
              [0.09376918234856364, 0.14039430098717853, 0.14330944292182635], [0.08033180078416728, 0.12000639900412913, 0.12214152323268862]]
Disp_rob = [[0.80928933687005, 1.3561206925571525, 1.6875002924319773], [0.4939237431615288, 0.7941123049854566, 0.876825600854562],
            [0.3319162266183392, 0.5194384920525256, 0.5605730537153674], [0.24989775674731157, 0.3854917020128351, 0.4089105281589659],
            [0.20037248636314364, 0.30636849819998374, 0.321355850034329], [0.1672271130943, 0.2541644009009639, 0.26455112256608826],
            [0.12565279150937603, 0.1895393621251458, 0.1953596522929219], [0.10063298261814788, 0.15110651192192, 0.15482302712176266],
            [0.08392205964978466, 0.12562900612873423, 0.12820725491204496], [0.07197056840775033, 0.10750201229166524, 0.10939590856073905]]
N_arr = [30, 50, 75, 100, 125, 150, 200, 250, 300, 350]
H_arr = [2, 9, 18]
#for i in range(10):
#    n = N_arr[i]
#    X_white = np.random.normal(0, 1, n)
#    X_NEW = X_white
#    for k in range(2, n):
#        X_NEW[k] = a0 * X_white[k] + a1 * X_white[k - 1] + b1 * X_NEW[k - 1] + b2 * X_NEW[k - 2]
#    for j in range(3):
#        h = H_arr[j]
#        summ = 0
#        for s in range(n-h):
#            for t in range(n-h):
#                summ+=(gamma_2(D,gamma0,gamma,s-t+h)+gamma_2(D,gamma0,gamma,s-t-h)-2*gamma_2(D,gamma0,gamma,s-t))**2
#        Disp_class[i][j] = summ/(2*((n-h)**2))
#        Disp_rob[i][j] = summ*(10/((n-h)**2))*(1/((0.457+0.494/(n-h)+0.045/((n-h)**2))**2))*(np.pi**(-1/2)-(scipy.special.gamma(3/4)**2)/np.pi)*(scipy.special.gamma(3/4)**6)/(np.pi**3)
#        print('i',i, 'j',j)
print("Значения дисперсий оценок:")
print("Классическая:")
print(Disp_class)
print("Робастная:")
print(Disp_rob)

fig, ax = plt.subplots(figsize=(10,8))
plt.style.use('dark_background')
plt.title("Значение дисперсии для шага h = 2", fontsize=16)
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Величина лага",fontsize=16)
ax.set_ylabel("Значение семивариограммы", fontsize=16)
T = np.arange(0,10)
Disp_class_H1 = [Disp_class[i][0] for i in range(10)]
Disp_rob_H1 = [Disp_rob[i][0] for i in range(10)]
Disp_class_H2 = [Disp_class[i][1] for i in range(10)]
Disp_rob_H2 = [Disp_rob[i][1] for i in range(10)]
Disp_class_H3 = [Disp_class[i][2] for i in range(10)]
Disp_rob_H3 = [Disp_rob[i][2] for i in range(10)]
plt.plot(T, Disp_class_H1, label = 'Классическая оценк')
plt.plot(T, Disp_rob_H1, label = 'Робастная оценка')
ax.legend()
plt.show()

fig, ax = plt.subplots(figsize=(10,8))
plt.style.use('dark_background')
plt.title("Значение дисперсии для шага h = 9 ", fontsize=16)
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Величина лага",fontsize=16)
ax.set_ylabel("Значение семивариограммы", fontsize=16)
plt.plot(T, Disp_class_H2, label = 'Классическая оценк')
plt.plot(T, Disp_rob_H2, label = 'Робастная оценка')
ax.legend()
plt.show()

fig, ax = plt.subplots(figsize=(10,8))
plt.style.use('dark_background')
plt.title("Значение дисперсии для шага h = 18 ", fontsize=16)
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Величина лага",fontsize=16)
ax.set_ylabel("Значение семивариограммы", fontsize=16)
plt.plot(T, Disp_class_H3, label = 'Классическая оценк')
plt.plot(T, Disp_rob_H3, label = 'Робастная оценка')
ax.legend()
plt.show()

