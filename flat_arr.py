def flat(A, depth=1):
    arrays_idx = []
    for i in range(len(A)):
        if isinstance(A[i], list):
            arrays_idx.append(i)
        else:
            A[i] = [(A[i])]
    flatten_arr = []
    for inner_arr in (A):
        flatten_arr.extend(inner_arr)
    return flatten_arr


test_arr = [0, 1, [2, 3], 4, 5]
print(flat(test_arr))

print('a, b, c'.split(sep=""))
