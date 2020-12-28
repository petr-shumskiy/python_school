from timeit import timeit
A = [3, 2, 1, 4, 0, 12, -5, 14] * 10


n = len(A)

for i in range(n):
    idx_max = 0
    for j in range(1, n - i):
        if A[j] > A[idx_max]:
            idx_max = j
    A[n - i - 1], A[idx_max] = A[idx_max], A[n - i - 1]

arr = [1, 2, 3, 4]
arr.insert(1, 4)
print(arr)
