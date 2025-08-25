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
for i in range(2):
    phi_0 = h* f_yj(yj_arr[i],Xi[i])
    phi_1 = h* f_yj(yj_arr[i]+0.5*phi_0, Xi[i]+1/20)
    phi_2 = h* f_yj(yj_arr[i]+phi_0+2*phi_1,Xi[i]+h)
    yj_jp1 = yj_arr[i]+1/6*(phi_0+4*phi_1+phi_2)
    yj_arr.append(yj_jp1)
print("Начальные значения функции в узлах Xi по методу РК3:")
for i in range(3):
    print("X",str(i),":\t", yj_arr[i])
for i in range(2, N-1):
    yj_jp1 = yj_arr[i]+h*(23/12*f_yj(yj_arr[i],Xi[i])-4/3*(f_yj(yj_arr[i-1],Xi[i-1]))+5/12*(f_yj(yj_arr[i-2],Xi[i-2])))
    yj_arr.append(yj_jp1)
print("Значения функции в узлах Xi по методу Адамса:")
for i in range(N):
    print("X",str(i),":\t", yj_arr[i])
#print(yj_arr)