from pprint import pprint
h = 0.1
Xi = []
a = 0
b = 1
N = 11
for i in range (N):
    Xi.append(int(100*i*h)/100)
print("Узлы нашей сетки:")
pprint(Xi)
def f_yj(y_j_p1,x_j):
    return -x_j * x_j * y_j_p1 * y_j_p1 + (x_j * x_j - 0.5) / (1 + 0.5 * x_j) / (1 + 0.5 * x_j)
yj_arr = []
yj_arr.append(1)
for i in range(N-1):
    yj_jp1 = yj_arr[i]+1/30*f_yj(yj_arr[i],Xi[i])+2/30*f_yj(yj_arr[i]+3/40*f_yj(yj_arr[i],Xi[i]),Xi[i]+3/40)
    yj_arr.append(yj_jp1)
print("Значения функции в узлах Xi:")
for i in range(N):
    print("X",str(i),":\t", yj_arr[i])
print(yj_arr)