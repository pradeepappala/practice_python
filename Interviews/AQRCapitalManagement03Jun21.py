
#number n squares of 1 to n
# even, odd, prime

def keyFunOdd(x):
    return True if x % 2 else False

def keyFunEven(x):
    return True if x % 2 == 0 else False

def funA(n, key=keyFunOdd):
    return (i*i for i in range(1, n+1) if key(i))

print(funA(10, key=keyFunOdd))
# sorted(['ab'], key=lambda x: len(x))
g = funA(10, key=keyFunOdd)
# for i in g:
#     print(i)
# g.next()

print(next(g))
print(next(g))


def my_decorator(fn):
    def wrapper_function(a, b):
        print('test')
        fn(a, b)
    return wrapper_function


@my_decorator
def fn(a, b):
    print('original '+str(a+b))

fn(1, 2)