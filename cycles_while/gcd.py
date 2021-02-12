def gcd(a, b) -> int:
    '''
    calcucaltes the greatest common divisor
    :type a: int
    :type b: int
    '''
    while b != 0:
        a, b = b, a % b
    return a


print(gcd(16, 20))
