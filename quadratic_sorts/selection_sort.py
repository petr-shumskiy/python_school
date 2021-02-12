from timeit import timeit


def quick_sort(A):
    if len(A) <= 1:
        return A

    small = quick_sort(list(filter(lambda x: x < A[0], A)))
    medium = (list(filter(lambda x: x == A[0], A)))
    high = quick_sort(list(filter(lambda x: x > A[0], A)))

    return small + medium + high


def counting_sort(A):
    B = []
    F = [0] * (max(A) + 1)

    for i in range(len(A)):
        F[A[i]] += 1

    for digit in range(len(F)):
        for i in range(F[digit]):
            B.append(digit)
    return B


def Tester(func):
    counter = 1

    def inner(test_values, expected):
        nonlocal counter
        if func(test_values) == expected:
            print(f'#test{counter} is OK')
        else:
            print(f'#test{counter} is Failed')
            print(func(test_values), expected)
        counter += 1
    return inner


def selection_sort(A):
    n = len(A)
    for i in range(1, n):
        idx_max = 0
        for j in range(n - i + 1):
            if A[j] > A[idx_max]:
                idx_max = j
        A[n - i], A[idx_max] = A[idx_max], A[n - i]

    return A


sortTesterSlow = Tester(selection_sort)
sortTesterQuick = Tester(quick_sort)
sortTesterNative = Tester(sorted)
sortTesterCounting = Tester(counting_sort)

qoeff = 10**1

print(
    # timeit(lambda:
    #        sortTesterQuick(
    #            test_values=[3, 2, 1] * qoeff,
    #            expected=sorted([3, 2, 1] * qoeff)
    #        ), number=1),
    timeit(lambda:
           sortTesterSlow(
               test_values=[3, 2, 1] * qoeff,
               expected=sorted([3, 2, 1] * qoeff)
           ), number=1)

)
