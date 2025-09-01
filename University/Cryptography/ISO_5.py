import numpy as np
from numpy import random
from scipy.optimize import linear_sum_assignment

def kuhn(v):
    if used[v] == 1:
        return 0
    used[v] = 1
    for i in g[v]:
        if (mt[i] == -1) or (kuhn(mt[i])):
            mt[i] = v
            return 1
    return 0

n = 6
k = 6
mt = [-1]*k
cnt = 0
g = [[0,2,5],[3, 4, 5],[2,4],[2,3,5],[0,2,5],[1,4]]
for i in range(n):
    used = [0]*n
    if (kuhn(i)) == 1:
        cnt += 1
print(cnt)


f = [[4, 5, 2, 1, 5],[5 ,3 ,5 ,2 ,3 ],[1 ,2 ,2 ,3 ,2],[4, 4 ,1 ,4, 3],[1 ,1 ,3 ,1 ,1]]
f_const = [[4, 5, 2, 1, 5],[5 ,3 ,5 ,2 ,3 ],[1 ,2 ,2 ,3 ,2],[4, 4 ,1 ,4, 3],[1 ,1 ,3 ,1 ,1]]
print("Исходная матрица")
for row in f:
    for elem in row:
        print(elem, end = ' ')
    print()
for i in range(len(f)):
    min_value = min(f[i])
    for j in range(len(f)):
        f[i][j] = f[i][j] - min_value
f = np.transpose(f)
for i in range(len(f)):
    min_value = min(f[i])
    for j in range(len(f)):
        f[i][j] = f[i][j] - min_value
f = np.transpose(f)
line_count = 0
while line_count < len(f):
    line_count = 0
    row_zero_count = []
    col_zero_count = []
    for i in range(len(f)):
        row_zero_count.append(np.sum(f[i] == 0))
    for i in range(len(f)):
        col_zero_count.append((np.sum(f[:, i] == 0)))
    line_order = []
    row_or_col = []
    for i in range(len(f), 0, -1):
        while i in row_zero_count:
            line_order.append(row_zero_count.index(i))
            row_or_col.append(0)
            row_zero_count[row_zero_count.index(i)] = 0
        while i in col_zero_count:
            line_order.append(col_zero_count.index(i))
            row_or_col.append(1)
            col_zero_count[col_zero_count.index(i)] = 0
    delete_count_of_row = []
    delete_count_of_col = []
    row_and_col = [i for i in range(len(f))]
    print(line_order)
    for i in range(len(line_order)):
        if row_or_col[i] == 0:
            delete_count_of_row.append(line_order[i])
        else:
            delete_count_of_col.append(line_order[i])
        c = np.delete(f, delete_count_of_row, axis=0)
        c = np.delete(c, delete_count_of_col, axis=1)
        line_count = len(delete_count_of_row) + len(delete_count_of_col)
        print(line_count)
        if line_count == len(f):
            break
        if 0 not in c:
            row_sub = list(set(row_and_col) - set(delete_count_of_row))
            min_value = np.min(c)
            for i in row_sub:
                f[i] = f[i] - min_value
            for i in delete_count_of_col:
                f[:, i] = f[:, i] + min_value
            print(f)
            break
row_ind, col_ind = linear_sum_assignment(f)
min_sum = 0
print(f)
for i in range(len(f_const)):
    min_sum += f_const[row_ind[i]][col_ind[i]]
    f_const[row_ind[i]][col_ind[i]] = str(f_const[row_ind[i]][col_ind[i]])+'*'
print("Минимальная стоимость:", min_sum)
print("Решение:", )
for i in range(len(f_const)):
    print(f_const[i])
