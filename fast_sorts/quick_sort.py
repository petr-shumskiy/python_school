# def qc(a):
#     if len(a) < 2:
#         return a
#     return (
#         qc(list(filter(lambda x: x < a[0], a)))
#         + list(filter(lambda x: x == a[0], a))
#         + qc(list(filter(lambda x: x > a[0], a)))
#     )


a = [1, 5, 0, 3, -8, 2]
print(qc(a))


def qc(a):
    if len(a) < 2:
        return a
    return(
        qc(filter(lambda x: x < a[0])) +
        qc(filter(lambda x: x == a[0])) +
        qc(filter(lambda x: x > a[0]))
    )
