from timeit import timeit
from random import randint


class Test():
    counter = 1

    def __init__(self, func):
        self.func = func

    def case(self, test_values, expected):
        print(test_values)
        ans = self.func(test_values)
        if ans == expected:
            time = self.timeit_(test_values)
            print(f'\tTest{self.counter} is OK\t{time} sec')
        else:
            print(f'Test{self.counter} is Failed')
            print(f'\tExpected: {expected}')
            print(f'\tReal: {ans}')

        self.counter += 1

    def random_case(self, start, end, num):
        random_values = [randint(start, end) for i in range(num)]
        ans = sorted(random_values)
        self.case(random_values, ans)

    def timeit_(self, test_values):
        return timeit(lambda: self.func(test_values), number=50)

    def timeit(self, test_values):
        time = timeit(lambda: self.func(test_values), number=50)
        print(f'{time} sec')

    def test(self):
        self.case(
            test_values=[1, 2, 3, 4],
            expected=sorted([1, 2, 3, 4])
        )
        self.case(
            test_values=[-1, -2, -3, -4],
            expected=sorted([-1, -2, -3, -4])
        )
        self.case(
            test_values=[],
            expected=sorted([])
        )
        self.case(
            test_values=[0],
            expected=sorted([0])
        )
        self.random_case(-100, 100, 100)
        self.random_case(-1000, 1000, 1000)
        self.random_case(-10, 10, 1000)
