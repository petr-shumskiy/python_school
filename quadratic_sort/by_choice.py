# from keys_funcs import sum_of_digits

# A = [3, 2, 1, 4, 0, 12, 5, 14]
# n = len(A)

# for i in range(1, n):
#     while sum_of_digits(A[i]) < sum_of_digits(A[i - 1]) and i > 0:
#         A[i], A[i - 1] = A[i - 1], A[i]
#         i -= 1
# print(A)


# arr = ['vasya_2000', 'sasha_1998', 'lesha_2007']
# arr2 = ['lg_$2000', 'samsung_$1900', 'xiaomi_$1777']
# print(sorted(arr2, key=lambda x: x.split('_')[1]))
from Test import Test
arr = [1, 2, 3, 0, 1, 2, 0, 3, 0, 5, 3, 1, 8]
# n = len(arr)

# for i in range(n):
#     for j in range(n):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]


def counting_sort(A):
    B = []
    F = [0] * len(A)

    for i in range(len(A)):
        F[A[i]] += 1

    for digit in range(len(F)):
        for i in range(F[digit]):
            B.append(digit)
    return B


res = counting_sort(arr)
print(res)
== == == =


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
