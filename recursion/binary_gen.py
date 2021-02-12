a = [0] * 3


def rec(i):
    i -= 1
    if i >= 0:
        a[i] = 0
        rec(i-1)
        a[i] = 1
        rec(i-1)
    print(a)


rec(3)
print(24//25)
