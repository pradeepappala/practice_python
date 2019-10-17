# calc module


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def pow(a, b):
    return a ** b


def main():
    a = 2
    b = 3
    print('add {}, {} is {}'.format(a, b, add(a, b)))
    print('sub {}, {} is {}'.format(a, b, sub(a, b)))
    print('mul {}, {} is {}'.format(a, b, mul(a, b)))
    print('pow {}, {} is {}'.format(a, b, pow(a, b)))

class MyClass:
    @property
    def last_transaction(self):
        # an expensive and complicated DB query here
        pass


if __name__ == '__main__':
    main()
