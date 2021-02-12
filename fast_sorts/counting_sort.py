def counting_sort(A):
    B = []
    F = [0] * (max(A) + 1)

    for i in range(len(A)):
        F[A[i]] += 1

    for digit in range(len(F)):
        for i in range(F[digit]):
            B.append(digit)
    return B


res = counting_sort([1, 3, 2, 4, 8, 0, 23, 12, 45, 0, 2, 3, 5])
print(res)
