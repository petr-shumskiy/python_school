test = [1, 2, 6, 3, -4, 4, 8, 5, -6] * 10 ** 3
filtered_test = list(filter(lambda x: x < 4, test))


def quick_sort(A):
    if len(A) <= 1:
        return A

    small = quick_sort(list(filter(lambda x: x < A[0], A)))
    medium = (list(filter(lambda x: x == A[0], A)))
    high = quick_sort(list(filter(lambda x: x > A[0], A)))

    return small + medium + high


print(quick_sort(test))
