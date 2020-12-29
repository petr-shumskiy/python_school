from Test import Test


def anonymus(arr):
    A = arr.copy()
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]
    return A


tester = Test(anonymus)
tester.test()
