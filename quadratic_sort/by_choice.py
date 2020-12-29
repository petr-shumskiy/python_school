from Test import Test


def sort_by_choice(arr):
    A = arr.copy()
    n = len(A)
    for i in range(1, n):
        while A[i] < A[i - 1] and i > 0:
            A[i], A[i - 1] = A[i - 1], A[i]
            i -= 1
    return(A)


tester = Test(sort_by_choice)
tester._show_preview()
