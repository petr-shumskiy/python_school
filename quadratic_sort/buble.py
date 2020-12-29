from Test import Test


def buble_sort(arr: list) -> list:
    '''
    Buble sort algorithm
    Takes an array and return new sorted array
    '''
    A = arr.copy()
    n = len(A)

    for i in range(n-1):
        swaped = False
        for j in range(1, n - i):
            if A[j - 1] > A[j]:
                A[j - 1], A[j] = A[j], A[j - 1]
                swaped = True

        if not swaped:
            return A
    return A


tester = Test(buble_sort)
tester.test()
