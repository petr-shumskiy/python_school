def pseudo_max(arr):
    real_max = max(arr[0], arr[1])
    pseudo_max = min(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] > real_max:
            pseudo_max = real_max
            real_max = arr[i]
        elif arr[i] > pseudo_max:
            pseudo_max = arr[i]

    return pseudo_max


class TestFunction():
    _counter = 1

    def __init__(self, func, counter=1):
        self._func = func
        self._counter = counter

    def case(self, test, expected):
        if self._func(test) == expected:
            print(f'#test{self._counter} OK')
        else:
            print(f'#test{self._counter} Failed')
        self._counter += 1


def test():
    pseudo_max_test = TestFunction(pseudo_max)
    pseudo_max_test.case(
        test=[1, 2, 3, 4, 5],
        expected=4
    )
    pseudo_max_test.case([-1, -2, -3, -4, -5], -2)
    pseudo_max_test.case([3, 6, 4, -10, 2], 4)
    pseudo_max_test.case([3, 6, 4, -10, 2, 0, 5], 5)


test()
