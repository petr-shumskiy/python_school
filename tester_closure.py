def TestCreator(func):
    x = 1

    def inner():
        nonlocal x
        print(x)
        x += 1
    return inner


def foo():
    print()


test = TestCreator(foo)
test()
test()
test()
test()
