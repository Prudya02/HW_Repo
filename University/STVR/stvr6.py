import math
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
sample_3 = [11.8,13.2,11.7,12.3,11.5,11.5,11.3,11.5,11.7,11.8,11.6,12.2,11.4,11.6,11.9,11.1,11.2,11.1,10.5,10.5,11.0,11.3,
            11.0,12.4,11.5,10.4,11.0,11.3,11.1,11.6,11.5,11.6,11.0,11.0,11.6,10.6,11.6]
r = [0 for i in range(19)]
T = len(sample_3)
for s in range(0, 19):
    k = 1/(T-s)
    suml = sum(sample_3[:T-s-1])
    suml_s = sum(sample_3[s:T-1])
    print(suml)
    up = 0
    left = 0
    right = 0
    for t in range(T-s):
        up += (sample_3[t]-k*suml)*(sample_3[t+s]-k*suml_s)
        left += (sample_3[t]-k*suml)**2
        right += (sample_3[t+s]-k*suml_s)**2
    left = math.sqrt(left*k)
    right = math.sqrt(right*k)
    up = up*k
    r[s] = up/(left*right)
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10,8))
ax.set_title('Автокорелляционная функция')
ax.grid(linestyle = "dashed", alpha = 0.2)
ax.set_xlabel("Сдвиг", fontsize=16)
ax.set_ylabel("Значение корреляции", fontsize=16)
x = np.arange(0, 19)
plt.plot(x, r)
plt.show()