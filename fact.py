def factorial(n):
    if n == 1:
        return n
    return factorial(n-1) * n


print(factorial(6))
j = 1
for i in range(1, 7):
    j *= i
print(j)
