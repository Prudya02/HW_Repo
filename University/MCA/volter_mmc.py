import numpy as np
from pprint import pprint
N = 10
a = 0
b = np.pi/2
h = (b-a)/(N-1)
y_array = np.array([[0.0] * N] * N)
Ai = [h]*10
f_array =np.array([0.0]*N)

for i in range (N):
    f_array[i] = 1+np.sin(i*h)
    for j in range(i+1):
        if (i == j):
            y_array[i][j] = 1 - Ai[j] * np.sin(i * h + h * j)
         # y_array[i][j] = int((1 - Ai[j]*np.sin(i*h + h*j))*1000)/1000
        else:
            y_array[i][j] = -Ai[j] * np.sin(i * h + h * j)
         # y_array[i][j] = int((-Ai[j]*np.sin(i*h + h*j))*1000)/1000
print("Матрица коэффициентов:")
pprint(y_array)
print("Вектор f:")
pprint(f_array)
y_solution = np.linalg.solve(y_array, f_array)
print("Приближенные решения:")
pprint(y_solution)

b2 = np.pi/4.4
h2 = (b2-a)/(N-1)
y_array2 = np.array([[0.0] * N] * N)
A2 = [h2]*10
f_array2 = np.array([0.0]*N)
for i in range (N):
    f_array2[i] = 1+np.sin(i*h2)
    for j in range(i+1):
        if (i == j):
            y_array2[i][j] = 1 - A2[j] * np.sin(i * h2 + h2 * j)
         # y_array[i][j] = int((1 - Ai[j]*np.sin(i*h + h*j))*1000)/1000
        else:
            y_array2[i][j] = -A2[j] * np.sin(i * h2 + h2 * j)
         # y_array[i][j] = int((-Ai[j]*np.sin(i*h + h*j))*1000)/1000
y_solution2 = np.linalg.solve(y_array2, f_array2)
print("Решение в точке xf:", y_solution2[N-1])