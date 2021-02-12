import math


input_number = int(input('input number for factorizing: '))
d = 2
while input_number > 1:
    if input_number % d == 0:
        print(d, end=' ')
        input_number //= d
    else:
        d += 1

lst = []
