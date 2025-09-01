#Вариант 5
#max 3x1 + 8x2 + 14x3
#2x1 + 3x2 + 5x3 ≤ 9; x1, x2, x3 ≥ 0 — целые.

n = 3
W = 100
v = [0, 3, 8, 14]
w = [0, 2, 3, 5]
f = [[0 for _ in range(W+1)] for _ in range(n+1)]
p = [[0 for _ in range(W+1)] for _ in range(n+1)]
ans = []
def Knaspack(i,c):
    if c < w[i]:
        return Knaspack(i-1,c)
    else:
        return max(f[i-1][c], f[i][int(c)-w[i]]+v[i])
for i in range (1, n+1):
    for c in range (0,W+1):
        f[i][c] = Knaspack(i,c)
for i in range(n+1):
    print(f[i])