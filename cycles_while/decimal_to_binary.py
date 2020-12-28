number = int(input())

binary = ''
while number != 0:
    binary += str(number % 2)
    number //= 2
    
print(binary[::-1])
