def fast_pow(x, n):
    if n < 1:
        return 1
    elif n % 2 == 0:
        return fast_pow(x**2, n//2)
    return x * fast_pow(x, n-1)


print(fast_pow(2, 10000))
