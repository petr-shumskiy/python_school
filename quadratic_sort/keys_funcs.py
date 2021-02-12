def sum_of_digits(num):
    if num < 0:
        num *= -1
    return sum(map(int, list(str(num))))
