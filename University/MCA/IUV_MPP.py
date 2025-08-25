import numpy as np
from pprint import pprint
n = 5
N = 10
a = 0
l = 1
xf = np.pi/4.4
b = np.pi/2
h = (b-a)/(N-1)
phi = np.array([[0.0] * N]*(n+1))
xi = []
phi_f = np.array([0.0]*6)
phi_f[0] = 1+np.sin(xf)
for i in range (N):
    xi.append(i*h)
    phi[0][i] = (1+np.sin(i*h))
print("Значения phi0 в узлах Xi:")
pprint(phi[0])
for i in range (1, n+1):
    for j in range(N):
        sum = 0
        sum2 = 0
        for k in range(0, j+1):
            sum += np.sin(xi[j]+xi[k])*phi[i-1][k]
            if (xi[k]<=xf):
                sum2 += np.sin(xf + xi[k]) * phi[i - 1][k]
        phi[i][j] = h*sum
        phi_f[i] = h*sum2
    print("Значения phi",i," в узлах Xi:")
    pprint(phi[i])
y_solution = [0.0]*N
for j in range(N):
    for i in range(n+1):
        y_solution[j] += (phi[i][j]*l)
print("Значения функции в узлах xi:")
pprint(y_solution)
y_f = 0
print(phi_f)
for i in range(n + 1):
    y_f += (phi_f[i])
print("Значение в точке xf:", y_f)