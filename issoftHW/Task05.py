def k_min(A, k):
    if k < 0:
        return print("k должен быть больше 0")
    try:
        q = A[k]
    except Exception as e1:
        return print(e1)
    for i in A:
        try:
            i = int(i)
        except Exception as e2:
            return print(e2)
    L = [elem for elem in A if elem < q]
    M = [q]*A.count(q)
    R = [elem for elem in A if elem > q]
    if len(L) > k:
        return k_min(L, k)
    if len(L) + len(M) > k >= len(L):
        return q
    if k >= len(L) + len(M):
        return k_min(R, k - len(L) - len(M))

sample = [1.2, 3.1, 2, 4, 4, 4, 5]
k = int(input("Введите k: "))
print(k_min(sample, k-1))
