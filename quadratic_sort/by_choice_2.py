

def sort(A):
    n = len(A)
    for i in range(1, n):
        while A[i] < A[i - 1] and i > 0:
            A[i], A[i - 1] = A[i - 1], A[i]
            print(A)
            i -= 1


testArr = [11, 9, 8, 59, 98]
res = [11, 8, 9, 59, 98]
sort(testArr)
