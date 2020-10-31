number = int(input('input number greater than 1: '))
divider = 2

while number % divider != 0:
    divider += 1

if number == divider:
    print('Prime')
else:
    print('Composite')
