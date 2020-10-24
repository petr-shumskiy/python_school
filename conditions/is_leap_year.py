year = int(input('Input the year: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('The year', year, 'is a leap')
else:
    print('The year', year, 'isn\'t a leap')
