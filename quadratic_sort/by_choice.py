A = [3, 2, 1, 4, 0, 12, -5, 14]
n = len(A)

for i in range(1, n):
    while A[i] < A[i - 1] and i > 0:
        A[i], A[i - 1] = A[i - 1], A[i]
        i -= 1
print(A)
b
