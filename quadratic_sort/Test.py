from timeit import timeit
from random import randint


class Test():
    counter: int = 1
    test_results: list = []

    def __init__(self, func):
        self.func = func

    def preview_values(self, values: list):
        if len(values) > 22:
            print('[', end='')
            print(*values[:10], sep=', ', end='')
            print(f' (... {len(values)} values more) ', end='')
            print(*values[-10:], sep=', ', end='')
            print(']')
        else:
            print(values)

    def case(self, test_values, expected):
        '''
        One test case, autoincrementing the number of a test
        '''
        self.preview_values(test_values)
        ans = self.func(test_values)
        if ans == expected:
            time = self._timeit(test_values)
            print(f'\tTest{self.counter} is OK\t{time} sec')

            self.test_results.append(True)
        else:
            print(f'Test{self.counter} is Failed')
            print('\tExpected: ', end='')
            self.preview_values(expected)
            print(f'\tReal: ', end='')
            self.preview_values(ans)

            self.test_results.append(False)

        self.counter += 1

    def random_case(self, start, end, num):
        random_values = [randint(start, end) for i in range(num)]
        ans = sorted(random_values)
        self.case(random_values, ans)

    def _timeit(self, test_values, number=5):
        return round(timeit(lambda: self.func(test_values), number=number) / number, 6)

    def _show_preview(self):
        for (num_of_test, is_passed) in enumerate(self.test_results, start=1):
            if is_passed:
                print(f'Test #{num_of_test} is OK')
            else:
                print(f'Test #{num_of_test} is Failed')

    def test(self):
        self.case(
            test_values=[1, 4, 3, 0, 9, 2, 12, 3],
            expected=sorted([1, 4, 3, 0, 9, 2, 12, 3])
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
        self.case(
            test_values=[i + 1 for i in range(10**4)],
            expected=[i + 1 for i in range(10**4)]
        )
        self.case(
            test_values=[i for i in range(10**4-1, -1, -1)],
            expected=sorted([i for i in range(10**4-1, -1, -1)])
        )

        self._show_preview()
