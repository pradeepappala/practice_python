
def get_n_primes(n):
    '''
    returns n prime numbers from start
    :param n: number of primes required
    :return list: returns list of first n prime numbers
    '''
    # start with first prime
    p = 2
    res = [2]
    for i in range(n-1):
        # get next prime
        p = get_next_prime(p)
        res.append(p)
    return res


def get_next_prime(n):
    '''
    get next prime number after n
    :param n:
    :return int : returns next prime after n
    '''
    while not is_prime(n+1):
        n = n + 1
    return n + 1


def is_prime(n):
    return not any([True if n % i == 0 else False for i in range(2, n//2+1)])


if __name__ == '__main__':
    q = get_n_primes(3)
    a = list(range(1,11))
    b = []
    j = 0
    for i in q:
        b.append([x for x in a if x % i == 0])
        a = [x for x in a if x not in b[-1]]
        print(*(b[-1][::1] if j % 2 == 0 else b[-1][::-1]), sep='\n')
        j = j + 1
    print(*a[::1], sep='\n')

