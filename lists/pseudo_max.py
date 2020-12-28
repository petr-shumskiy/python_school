lst = [3, 6, 2, 4, 2, 1]

real_max = max(lst[0], lst[1])
pseudo_max = min(lst[0], lst[1])

for i in range(2, (lst)):
    element = lst[i]

    if element > real_max:
        pseudo_max = real_max
        real_max = element
    elif element > pseudo_max:
        pseudo_max = element

print(lst)
print(real_max)
print(pseudo_max)
