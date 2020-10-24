n = int(input('Input the number for convert: '))

if n == 0:
    print('0')
elif n < 4:
    print('I' * n)
elif n == 4:
    print('IV')
elif n < 9:
    print('V' + 'I' * (n - 5))
elif n == 9:
    print('IX')
