arr = list(map(int, input().split(', ')))

real_max = max(arr[0], arr[1])
pseudo_max = min(arr[0], arr[1])

for i in range(2, len(arr)):
    if arr[i] > real_max:
        pseudo_max = real_max
        real_max = arr[i]
    elif arr[i] > pseudo_max:
        pseudo_max = arr[i]

print(pseudo_max)
