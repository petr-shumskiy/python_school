from Test import Test


# def sort(A):
#     n = len(A)
#     for i in range(n):
#         idx_max = 0
#         for j in range(1, n - i):
#             if A[j] > A[idx_max]:
#                 idx_max = j
#         A[n - i - 1], A[idx_max] = A[idx_max], A[n - i - 1]
#     return A

def sort(A):
    n = len(A)
    for i in range(n):
        cm = 0
        for j in range(1,  n - i):
            if A[j] > A[cm]:
                cm = j
        A[n-i-1], A[cm] = A[cm], A[n-i-1]
    return A


test_sort = Test(sort)
test_sort.test()
