import numpy as np

def NOD(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2

def NOK(a,b):
    return a*b/NOD(a, b)

def calc_time(T,nok):
    res = 0
    while (T > res):
        res+=nok
    return res
fin = open('input.txt')
n = int(fin.read(1))
m = int(fin.read(2))
data = []
R1, T1, R2, T2 = [[0]*(m) for _ in range(4)]
for line in fin:
    data.append([int(x) for x in line.split()])
print(data[1:])
for i in range (m):
    R1[i] = data[i+1][0]
    T1[i] = data[i+1][1]
    R2[i] = data[i+1][2]
    T2[i] = data[i+1][3]
print("R1:", R1)
print("R2:", R2)
print("T1:", T1)
print("T2:", T2)
kG = [0]*m
G = [[0]*m for i in range(m)]
P = [[0]*m for i in range(m)]
for i in range(m):
    kG[R1[i]-1] += 1
    G[R1[i]-1][kG[R1[i]-1]-1] = R2[i]
    P[R1[i]-1][kG[R1[i]-1]-1] = NOK(T1[i], T2[i])
    kG[R2[i]-1] += 1
    G[R2[i]-1][kG[R2[i]-1]-1] = R1[i]
    P[R2[i]-1][kG[R2[i]-1]-1] = NOK(T1[i], T2[i])
print("Весовая матрица")
for i in range(len(P)):
        print(P[i], '\t')
print(kG)
print("Граф:")
for i in range(len(G)):
        print(G[i], '\t')
print('\n')
versh = [1]*n
parent = [1]*n
dist = [np.inf]*n
versh[0] = 2
parent[0] = 0
dist[0] = 0
Blizh = 0
print("Расстояния на j-ом шаге:")
for j in range(kG[0]):
    dist[G[0][j]-1] = P[0][j]+0.5
for i in range(n-1):
    min_dist = np.inf
    for j in range(n):
        if versh[j] == 1 and dist[j] < min_dist:
            min_dist = dist[j]
            Blizh = j
        versh[Blizh] = 2
    for j in range(kG[Blizh]):
        if versh[G[Blizh][j]-1] == 1:
            new_time = calc_time(dist[Blizh], P[Blizh][j])
            if dist[G[Blizh][j]-1] > new_time+0.5:
                dist[G[Blizh][j]-1] = new_time+0.5
                parent[G[Blizh][j]-1] = Blizh+1
    print(i, dist)
tg = n
i = 0
path = [0]*n
while tg != 1:
    path[i] = tg
    tg = parent[tg-1]
    i += 1
print(f"Оптимальное время: {dist[-1]}")
path = path[::-1]
print("Искомая последовательность", (path[(len(path)-i):]))

